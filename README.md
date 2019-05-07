## COOK_BE
### 目录说明
```
└─apps                          各app集合处
└─log                           日志文件
└─media                         媒体文件
└─static                        静态资源文件
└─COOK_BE                      项目文件
    │  settings.py              配置文件
    │  urls.py                  路由
    │  wsgi.py                  作为项目的运行在 WSGI 兼容的Web服务器上的入口
    │  __init__.py              空文件，告诉 Python 这个目录应该被认为是一个 Python 包
│  manage.py                    管理 Django 项目的命令行工具
│  README.md                    README
│  db.sqlite3                   自带数据库文件
```

### 错误码

| 代码 | 状态 |
| -- | -- |
| 101 | 邮箱已存在 |
| 102 | 邮箱不存在 |
| 1000 | 成功 |
| 1001 | 表单验证失败 |
| 1002 | 字段不存在 |
| 2001 | 账户密码不匹配 |
| 3001 | 字段不能为空 |
| 4001 | 上传文件失败 |
