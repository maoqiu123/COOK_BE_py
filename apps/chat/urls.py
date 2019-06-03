# _*_ coding: utf-8 _*_
from django.urls import path
from django.conf.urls import url, include
from .views import ChatView

urlpatterns = [
    url('^bind/?$', ChatView.as_view()),
]
