# _*_ coding: utf-8 _*_
from django.urls import path
from django.conf.urls import url, include

from users.views import RegisterView, LoginView, UserView, TestView
from chat.views import ChatView
import chat.urls as chat

urlpatterns = [
    url('^register/?$', RegisterView.as_view()),
    url('^login/?$', LoginView.as_view()),
    url('^user/?$', UserView.as_view()),

    url('^test/?$', TestView.as_view()),
]