# _*_ coding: utf-8 _*_
from users.models import User
from hashlib import md5
from datetime import datetime, timedelta


def make_token(email):
    my_str = str(datetime.now())
    my_str = my_str + email
    m5 = md5()
    m5.update(my_str.encode("utf8"))
    token = m5.hexdigest()

    user = User.objects.filter(email=email)[0]
    token_expire = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%I:%S')
    user.token = token
    user.token_expire = token_expire
    user.save()
    return token


def check_token_exists(token):
    user = User.objects.filter(token=token)
    if user.exists():
        return 0
    else:
        return 201


def check_token(token):
    code = check_token_exists(token)
    if code == 201:
        return 201
    user = User.objects.filter(token=token)[0]
    token_expire = user.token_expire
    if token_expire >= datetime.now():
        # make_token(user.email)
        return user
    else:
        return 202
