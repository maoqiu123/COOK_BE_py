# _*_ coding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    avatar = models.ImageField(max_length=100, verbose_name=u"用户头像", null=True, blank=True)
    token = models.CharField(max_length=200, verbose_name=u"用户token", null=True, blank=True)
    token_expire = models.DateTimeField(default=datetime.now, verbose_name=u"token过期时间", null=True, blank=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
        db_table = "users"

    def __str__(self):
        return self.username
