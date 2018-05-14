
from datetime import datetime

from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称", null=False, blank=False)
    desc = models.CharField(max_length=100, verbose_name=u"描述", null=False, blank=False)
    detail = models.TextField(verbose_name=u"机构介绍")
    course_nums = models.IntegerField(default=0,verbose_name=u"课程数")
    students_nums = models.IntegerField(default=0,verbose_name=u"学习人数")
    address = models.CharField(null=False,blank=False,verbose_name=u"机构地址",max_length=255)
    organ_icon = models.ImageField(upload_to="organization/%Y/%m",verbose_name=u"机构图标",max_length=125)

    fav_nums = models.IntegerField(verbose_name=u"收藏数")
    org_click_nums = models.IntegerField(verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(Organization,verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名称", null=False, blank=False)
    desc = models.CharField(max_length=100, verbose_name=u"描述", null=False, blank=False)
    tea_icon = models.ImageField(upload_to="organization/%Y/%m",verbose_name=u"教师图标",max_length=125)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    work_years = models.IntegerField(verbose_name=u"工作年限")
    work_company = models.CharField(verbose_name=u"在职公司",max_length=20)
    work_position = models.CharField(verbose_name=u"在职岗位",max_length=20)
    work_points = models.CharField(max_length=100,verbose_name=u"教学特点")

    fav_nums = models.IntegerField(verbose_name=u"收藏数")
    tea_click_nums = models.IntegerField(verbose_name=u"点击数")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name