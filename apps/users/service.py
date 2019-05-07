# _*_ coding: utf-8 _*_
from users.models import User
from django.contrib.auth.hashers import make_password, check_password
from hashlib import md5
from datetime import datetime, timedelta


def register(request):
    user = User()
    user.email = request.POST.get("email", "")
    user.username = request.POST.get("username", "")
    user.password = make_password(request.POST.get("password", ""))
    user.save()


def check_email(email):
    status = User.objects.filter(email=email)
    if status.exists():
        return 101
    return 0


def login(request):
    email = request.POST.get("email", "")
    code = check_email(email)
    if code != 101:
        return 102
    user = User.objects.filter(email=email)[0]
    if check_password(request.POST.get("password", ""), user.password):
        token = make_token(email)
        token_expire = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%I:%S')
        user.token = token
        user.token_expire = token_expire
        user.save()
    else:
        return 2001
    return token


def make_token(email):
    my_str = str(datetime.now())
    my_str = my_str + email
    m5 = md5()
    m5.update(my_str.encode("utf8"))
    data = m5.hexdigest()
    return data



