# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
    time:2018/5/13 下午7:39
"""
import xadmin
from .models import Course,LessonVideo,Lesson,CourseResource


class CourseAdmin(object):
    pass


class LessonAdmin(object):
    pass


class LessonVideoAdmin(object):
    pass


class CourseResourceAdmin(object):
    pass

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(LessonVideo,LessonVideoAdmin)