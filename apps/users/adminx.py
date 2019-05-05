# _*_ coding: utf-8 _*_
__author__ = 'maoqiu'
__data = '2019/5/4 15:13'

import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "COOK后台管理系统"
    site_footer = "毛球提供"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
