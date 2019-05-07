# _*_ coding: utf-8 _*_
from django.http import HttpResponse
import json


def response(code, message, data):
    result = {"code": code, "message": message, "data": data}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def response_form(code, message, data):
    for key, value in message.items():
        message = key + ": " + value[0]
    result = {"code": code, "message": message, "data": data}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")