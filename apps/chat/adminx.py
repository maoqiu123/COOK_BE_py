# _*_ coding: utf-8 _*_
import xadmin
from xadmin import views
from .models import Group


class GroupAdmin(object):
    list_display = ['chat_id', 'group_id', 'group_name']
    search_fields = ['chat_id', 'group_id', 'group_name']
    list_filter = ['chat_id', 'group_id', 'group_name']


xadmin.site.register(Group, GroupAdmin)
