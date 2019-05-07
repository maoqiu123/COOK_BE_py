# _*_ coding: utf-8 _*_
from users.models import User
from django.contrib.auth.hashers import make_password, check_password


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
