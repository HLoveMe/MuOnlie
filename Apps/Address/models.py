from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"名称")
    desc = models.TextField(verbose_name=u"描述")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"国家"
        verbose_name_plural = verbose_name


class Province(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"名称")
    desc = models.TextField(verbose_name=u"描述")
    country = models.ForeignKey(Country,verbose_name=u"国家",default=-1)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"州/省/直辖市"
        verbose_name_plural = verbose_name


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"名称")
    code = models.CharField(max_length=20,verbose_name=u"邮政编码")
    desc = models.TextField(verbose_name=u"描述")
    province = models.ForeignKey(Province, verbose_name=u"州/省/直辖市",default=-1)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


class Town(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"名称")
    desc = models.TextField(verbose_name=u"描述",default="")
    city = models.ForeignKey(Province, verbose_name=u"城市",default=-1)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"镇"
        verbose_name_plural = verbose_name


class Village(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"名称")
    desc = models.TextField(verbose_name=u"描述",default="")
    town = models.ForeignKey(Province, verbose_name=u"镇",default=-1)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"村"
        verbose_name_plural = verbose_name