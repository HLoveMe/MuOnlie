# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
    time:"2018/5/13 下午7:03"
"""

import xadmin
from .models import EmailVerify
from xadmin.views import BaseAdminView,CommAdminView



class EmailVerifyAdmin(object):
    refresh_times = (10,20)
    pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch=True
    pass



class GlobalSettings(object):
    site_title="猪猪管理系统"
    site_footer="朱子豪的Company"
    menu_style="accordion"


xadmin.site.register(EmailVerify,EmailVerifyAdmin);
xadmin.site.register(BaseAdminView,BaseSetting);
xadmin.site.register(CommAdminView,GlobalSettings);
