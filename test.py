import socket
import time
import hashlib
import base64
import struct
from multiprocessing import Process

HTTP_RESPONSE = "HTTP/1.1 {code} {msg}\r\n" \
                "Server:LyricTool\r\n" \
                "Date:{date}\r\n" \
                "Content-Length:{length}\r\n" \
                "\r\n" \
                "{content}\r\n"
STATUS_CODE = {200: 'OK', 501: 'Not Implemented'}
UPGRADE_WS = "HTTP/1.1 101 Switching Protocols\r\n" \
             "Connection: Upgrade\r\n" \
             "Upgrade: websocket\r\n" \
             "Sec-WebSocket-Accept: {}\r\n" \
             "WebSocket-Protocol: chat\r\n\r\n"


def sec_key_gen(msg):
    key = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    ser_key = hashlib.sha1(key.encode('utf-8')).digest()
    return base64.b64encode(ser_key).decode()


class WebsocketServer:
    def __init__(self, conn):
        # 接受一个socket对象  
        self.conn = conn
        self.state = 0

    def open(self):
        self._handshake()
        if self.state == 1:
            return self
        else:
            raise Exception('Handsake failed.')

    def __enter__(self):
        return self.open()

    def getstate(self):
        # 获取连接状态  
        state_map = {0: 'READY', 1: 'CONNECTION ESTABLISHED', 2: 'HANDSHAKED', 3: 'FAILED', -1: 'CLOSED'}
        return self.state, state_map[self.state]

    def _handshake(self):
        raw_data = b''
        while True:
            fragment = self.conn.recv(1024)
            raw_data += fragment
            if len(fragment) < 1024:
                break
        data = raw_data.decode('utf-8')
        header, content = data.split('\r\n\r\n', 1)
        header = header.split('\r\n')
        options = map(lambda i: i.split(': '), header[1:])
        options_dict = {item[0]: item[1] for item in options}
        date = time.strftime("%m,%d%Y", time.localtime())
        if 'Sec-WebSocket-Key' not in options_dict:
            self.conn.send(
                bytes(HTTP_RESPONSE.format(code=501, msg=STATUS_CODE[501], date=date, length=len(date), content=date),
                      encoding='utf-8'))
            self.conn.close()
            self.state = 3
            return True
        else:
            self.state = 2
            self._build(options_dict['Sec-WebSocket-Key'])
            return True

    def _build(self, sec_key):
        # 建立WebSocket连接  
        response = UPGRADE_WS.format(sec_key_gen(sec_key))
        self.conn.send(bytes(response, encoding='utf-8'))
        self.state = 1
        return True

    def _get_data(self, info, setcode):
        payload_len = info[1] & 127
        fin = 1 if info[0] & 128 == 128 else 0
        opcode = info[0] & 15  # 提取opcode  

        # 提取载荷数据  
        if payload_len == 126:
            # extend_payload_len = info[2:4]  
            mask = info[4:8]
            decoded = info[8:]
        elif payload_len == 127:
            # extend_payload_len = info[2:10]  
            mask = info[10:14]
            decoded = info[14:]
        else:
            # extend_payload_len = None  
            mask = info[2:6]
            decoded = info[6:]

        bytes_list = bytearray()
        for i in range(len(decoded)):
            chunk = decoded[i] ^ mask[i % 4]
            bytes_list.append(chunk)
        if opcode == 0x00:
            opcode = setcode
        if opcode == 0x01:  # 文本帧
            body = str(bytes_list, encoding='utf-8')
            return fin, opcode, body
        elif opcode == 0x08:
            self.close()
            raise IOError('Connection closed by Client.')
        else:  # 二进制帧或其他，原样返回  
            body = decoded
            return fin, opcode, body

    def recv(self):
        msg = ''
        # 处理切片  
        opcode = 0x00
        while True:
            raw_data = b''
            while True:
                section = self.conn.recv(1024)
                raw_data += section
                if len(section) < 1024:
                    break
            fin, _opcode, fragment = self._get_data(raw_data, opcode)
            opcode = _opcode if _opcode != 0x00 else opcode
            msg += fragment
            if fin == 1:  # 是否是最后一个分片
                break
        return msg

    def send(self, msg, fin=True):
        # 发送数据  
        data = struct.pack('B', 129) if fin else struct.pack('B', 0)
        msg_len = len(msg)
        if msg_len <= 125:
            data += struct.pack('B', msg_len)
        elif msg_len <= (2 ** 16 - 1):
            data += struct.pack('!BH', 126, msg_len)
        elif msg_len <= (2 ** 64 - 1):
            data += struct.pack('!BQ', 127, msg_len)
        else:
            # 分片传输超大内容（应该用不到）  
            while True:
                fragment = msg[:(2 ** 64 - 1)]
                msg -= fragment
                if msg > (2 ** 64 - 1):
                    self.send(fragment, False)
                else:
                    self.send(fragment)
        data += bytes(msg, encoding='utf-8')
        self.conn.send(data)

    def ping(self):
        ping_msg = 0b10001001
        data = struct.pack('B', ping_msg)
        data += struct.pack('B', 0)
        while True:
            self.conn.send(data)
            data = self.conn.recv(1024)
            pong = data[0] & 127
            if pong != 9:
                self.close()
                raise IOError('Connection closed by Client.')

    def close(self):
        self.conn.close()
        self.state = -1

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is IOError:
            print(exc_val)
        self.close()


def ws_handler(conn):
    with WebsocketServer(conn) as ws:
        while True:
            msg = ws.recv()
            if ws.state == -1:
                break
            print(msg)
            ws.send(str(msg.split(',')))


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', 1233))
    s.listen(1)
    print('Server Started.')
    while True:
        con, addr = s.accept()
        print("Accepted. {0}, {1}".format(con, str(addr)))
        p = Process(target=ws_handler, args=(con,))
        p.start()  