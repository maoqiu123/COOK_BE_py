# _*_ coding: utf-8 _*_
from django.utils.deprecation import MiddlewareMixin
from utils.TokenTool import check_token
from utils.ResponseTool import response


class Middle1(MiddlewareMixin):
    white_list = ['/login/', '/register/', "/xadmin/"]  # 白名单
    balck_list = ['/black/', ]  # 黑名单

    def process_request(self, request):
        from django.shortcuts import redirect, HttpResponse

        next_url = '/' + request.path_info.split('/', 2)[1] + '/'

        if next_url in self.white_list or request.session.get("user"):
            pass
        elif next_url in self.balck_list:
            return HttpResponse('This is an illegal URL')
        else:
            user = check_token(request.headers['Token'])
            if user == 201:
                return response(201, "token不存在", None)
            elif user == 202:
                return response(202, "token已过期", None)
            request.my_user = user


    def process_response(self, request, response):
        return response  # 执行完了这个中间件一定要 传递给下一个中间件



