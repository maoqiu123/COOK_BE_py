"""COOK_BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path
from django.conf.urls import url, include

from users.views import RegisterView, LoginView, UserView, TestView
from chat.views import ChatView
import chat.urls as chat
import users.urls as user

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url('', include(user)),
    # url('^register/?$', RegisterView.as_view()),
    # url('^login/?$', LoginView.as_view()),
    # url('^user/?$', UserView.as_view()),

    url('^chat/', include(chat)),
    #
    # url('^test/?$', TestView.as_view()),
]
