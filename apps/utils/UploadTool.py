# _*_ coding: utf-8 _*_
from qiniu import Auth, put_file, etag
from django.conf import settings
from PIL import Image
import io
import uuid

q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)


def upload(request):
    avat = request.FILES['pic'].read()
    size = len(avat) / (1024 * 1024)
    image = Image.open(io.BytesIO(avat))

    key = 'media/' + str(uuid.uuid1()).replace('-', '')

    name = 'upfile.{0}'.format(image.format)  # 获取图片后缀（图片格式）

    if size > 1:
        # 压缩
        x, y = image.size
        im = image.resize((int(x / 1.73), int(y / 1.73)), Image.ANTIALIAS)  # 等比例压缩 1.73 倍
    else:
        # 不压缩
        im = image

    im.save('./media/' + name)  # 在根目录有个media文件
    path = './media/' + name

    token = q.upload_token(settings.QINIU_BUCKET_NAME, key, 3600, )

    put_file(token, key, path)
    url = 'http://cook.thmaoqiu.cn/{}'.format(key)
    return url

