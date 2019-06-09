from django.shortcuts import render
from django.views.generic.base import View
from utils.ResponseTool import response
from .service import bind, groupBind, groupDeleteBind
# Create your views here.


class ChatView(View):
    def post(self, request):
        bind()
        return response(1000, 'test')


class GroupView(View):
    def post(self, request):
        groupBind(request)
        return response(1000, 'groupBind')

    def delete(self, request):
        groupDeleteBind(request)
        return response(1000, 'delete groupBind')
