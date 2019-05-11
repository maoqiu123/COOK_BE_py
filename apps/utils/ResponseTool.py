# _*_ coding: utf-8 _*_
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict


def response(code, message, data=None):
    result = {"code": code, "message": message, "data": data}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def response_object(code, message, data):
    data = model_to_dict(data)
    for item in data:
        data[item] = str(data[item])
    result = {"code": code, "message": message, "data": data}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def response_form(code, message, data):
    for key, value in message.items():
        message = key + ": " + value[0]
    result = {"code": code, "message": message, "data": data}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")