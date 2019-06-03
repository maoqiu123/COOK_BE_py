from django.shortcuts import render
from django.views.generic.base import View
from utils.ResponseTool import response
from .service import bind
# Create your views here.


class ChatView(View):
    def post(self, request):
        bind()
        return response(1000, 'test')
