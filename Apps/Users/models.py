

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    nick_name = models.CharField(
        max_length=50,
        verbose_name=u"昵称",
        default="",
        null=False,
        blank=False
    )
    birday = models.DateField(
        null=True,
        blank=True,
        verbose_name=u"生日"
    )
    gender = models.CharField(
        choices=(("male",u"男"),("women",u"女")),
        default="male",
        verbose_name=u"性别",
        max_length=10
    )
    address = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name=u"地址"
    )

    moblie = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name=u"手机号"
    )

    icon = models.ImageField(
        verbose_name=u"头像",
        upload_to="icons/%Y/%m/%d"
    )

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name
        pass


class EmailVerify(models.Model):
    code = models.CharField(max_length=6,verbose_name=u"验证码",null=False,blank=False,default="123456")
    email = models.EmailField(max_length=25,verbose_name=u"邮箱",null=False,blank=False,default="default@qq.com")
    code_type = models.IntegerField(choices=((0,u"注册"),(1,u"找回密码")),verbose_name=u"验证类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = "邮箱验证"
        verbose_name_plural = verbose_name
    pass
