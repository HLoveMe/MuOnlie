
from datetime import datetime

from django.db import models

from Apps.Users.models import UserProfile
from Apps.Course.models import Course
from Apps.Course.models import LessonVideo


class UserComment(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    superUser = models.ForeignKey(UserProfile, verbose_name=u"@的用户",null=True,blank=True,related_name="super_set")
    course = models.ForeignKey(Course,verbose_name=u"课程")
    content = models.CharField(max_length=200,verbose_name=u"评论内容")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name
        pass
    pass


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0,verbose_name=u"收藏对象ID")
    fav_type = models.IntegerField(choices=((1,u"课程"),(2,u"机构"),(3,u"教师")),verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"收藏"
        verbose_name_plural = verbose_name
        pass
    pass


class UserAsk(models.Model):
    """用户提交想学的信息"""
    name = models.CharField(max_length=20,verbose_name=u"姓名")
    mobile = models.CharField(max_length=11,verbose_name=u"手机号")
    course = models.CharField(max_length=25,verbose_name=u"课程名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户询问"
        verbose_name_plural = verbose_name
        pass
    pass


class UserMessage(models.Model):
    """
        0 : 表示所有用户消息
        值 : 某个用户消息
    """
    user = models.IntegerField(default=0,verbose_name=u"用户")
    content = models.CharField(max_length=200,verbose_name=u"消息")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    is_read = models.BooleanField(default=False,verbose_name=u"是否已读")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name
        pass

"""
    用户课程
"""


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name
        pass
    pass


"""
    记录用户播放时长
"""


class UserCourseVideo(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    video = models.ForeignKey(LessonVideo,verbose_name=u"学习视频")
    time = models.IntegerField(default=0,verbose_name=u"已经学习时长")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"学习时长"
        verbose_name_plural = verbose_name
        pass
    pass