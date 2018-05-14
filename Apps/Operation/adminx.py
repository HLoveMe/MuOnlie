# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
    time:2018/5/13 下午7:47
"""
from .models import UserMessage,UserComment,UserAsk,UserCourse

from Extra_Apps import xadmin


class UserMessageAdmin(object):
    pass


class UserCommentAdmin(object):
    pass


class UserAskAdmin(object):
    pass


class UserCourseAdmin(object):
    pass


xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserComment,UserCommentAdmin)
xadmin.site.register(UserAsk,UserAskAdmin)

