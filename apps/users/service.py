# _*_ coding: utf-8 _*_
from users.models import User
from django.contrib.auth.hashers import make_password, check_password
from utils.TokenTool import make_token


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
        return token
    else:
        return 2001


def update_user(request):
    user = User.objects.filter(email=request.my_user.email)[0]
    user.username = request.PUT.get('username')
    user.save()
    print(user)
    pass

