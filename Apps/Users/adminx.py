# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
    time:"2018/5/13 下午7:03"
"""

from Extra_Apps import xadmin

from .models import EmailVerify

class EmailVerifyAdmin(object):
    pass

xadmin.site.register(EmailVerify,EmailVerifyAdmin);