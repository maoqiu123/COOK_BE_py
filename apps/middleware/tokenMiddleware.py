# _*_ coding: utf-8 _*_
from django.utils.deprecation import MiddlewareMixin


class Middle1(MiddlewareMixin):
    white_list = ['/login/', '/register/', "/xadmin/"]  # 白名单
    balck_list = ['/black/', ]  # 黑名单

    def process_request(self, request):
        from django.shortcuts import redirect, HttpResponse

        next_url = '/' + request.path_info.split('/', 2)[1] + '/'

        print(request.path_info, request.get_full_path())
        if next_url in self.white_list or request.session.get("user"):
            pass
        elif next_url in self.balck_list:
            return HttpResponse('This is an illegal URL')
        else:
            print("pass")

    def process_response(self, request, response):
        print('走了')
        return response  # 执行完了这个中间件一定要 传递给下一个中间件



