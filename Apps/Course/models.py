# coding=utf-8

from django.db import models
from datetime import datetime
# Create your models here.
from Organization.models import Organization


class Course(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name="主键")
    name = models.CharField(max_length=50,verbose_name=u"名称",null=False,blank=False)
    desc = models.CharField(max_length=100,verbose_name=u"描述",null=False,blank=False)
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(choices=(("cj",u"初级"),("zj",u"中级"),("gj",u"高级")),max_length=5,verbose_name=u"难度",null=False,blank=False)
    learn_time = models.IntegerField(default=0,null=False,verbose_name=u"学习时长(min)")
    students_nums = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
    course_image = models.ImageField(upload_to="course/%Y/%h",verbose_name=u"课程图标")
    course_click_nums = models.IntegerField(verbose_name=u"课程点击量")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    organization = models.ForeignKey(Organization,verbose_name=u"机构")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name;
        pass
    pass


class Lesson(models.Model):
    course = models.ForeignKey(Course,to_field="id",verbose_name=u"课程")
    name = models.CharField(max_length=50,verbose_name=u"章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name;
    pass


class LessonVideo(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=50, verbose_name=u"视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name;


# 课程资源
class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=50, verbose_name=u"资源名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    download = models.FileField(verbose_name=u"资源地址",upload_to="course/%Y/%h")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name;
    pass