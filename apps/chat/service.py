# _*_ coding: utf-8 _*_
from chat.models import Group
from users.models import User


def bind():
    print(666)
    pass


def groupBind(request):
    group = Group()
    group.chat_id = request.POST.get('chat_id')
    group.save()
    return 1000


def groupDeleteBind(request):
    print('chat_id' + request.DELETE.get("chat_id"))
    gr = Group.objects.filter(chat_id=request.DELETE.get("chat_id"))
    if gr.exists():
        gr[0].delete()
    return 1000


def test():
    print(66666666666666666)


