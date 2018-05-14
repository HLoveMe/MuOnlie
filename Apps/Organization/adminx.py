# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
    time:2018/5/13 下午7:43
"""

from .models import Organization,Teacher

from Extra_Apps import xadmin


class OrganizationAdmin(object):
    pass


class TeacherAdmin(object):
    pass

xadmin.site.register(Organization,OrganizationAdmin)
xadmin.site.register(Teacher,TeacherAdmin)