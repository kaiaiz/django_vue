#encoding=utf-8

import xadmin
from xadmin import views

from .models import VerifyCode


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetiings(object):
    site_title = u"商店后台"
    site_footer = "yanchaomin"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSetiings)
