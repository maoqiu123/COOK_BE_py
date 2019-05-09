# _*_ coding: utf-8 _*_
from django.utils.deprecation import MiddlewareMixin
from django.http.multipartparser import MultiPartParser


class RestfulMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.method == 'PUT':
            put = MultiPartParser(request.META, request, request.upload_handlers).parse()
            request.PUT = put[0]

    def process_response(self, request, response):
        return response  # 执行完了这个中间件一定要 传递给下一个中间件





