# _*_ coding: utf-8 _*_
from django.utils.deprecation import MiddlewareMixin
from django.http.multipartparser import MultiPartParser
from django.http import QueryDict


class RestfulMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.body)
        if request.method == 'PUT':
            # put = QueryDict(request.body)
            # request.PUT = put
            # postman form-data传来的数据
            put = MultiPartParser(request.META, request, request.upload_handlers).parse()
            request.PUT = put[0]
        if request.method == 'DELETE':
            # delete = QueryDict(request.body)
            # request.DELETE = request.GET
            # postman form-data传来的数据
            delete = MultiPartParser(request.META, request, request.upload_handlers).parse()
            request.DELETE = delete[0]





