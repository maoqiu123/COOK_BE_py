# _*_ coding: utf-8 _*_
import xadmin
from xadmin import views
from .models import User


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "COOK后台管理系统"
    site_footer = "毛球提供"
    menu_style = "accordion"


class UserAdmin(object):
    list_display = ['username', 'email', 'password', 'avatar', 'token', 'token_expire']
    search_fields = ['username', 'email']
    list_filter = ['username', 'email']


xadmin.site.register(User, UserAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
