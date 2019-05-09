# _*_ coding: utf-8 _*_
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)


class UserUpdateForm(forms.Form):
    username = forms.CharField(required=True)
