# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-13 06:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('detail', models.TextField(verbose_name='机构介绍')),
                ('course_nums', models.IntegerField(default=0, verbose_name='课程数')),
                ('students_nums', models.IntegerField(default=0, verbose_name='学习人数')),
                ('address', models.CharField(max_length=255, verbose_name='机构地址')),
                ('organ_icon', models.ImageField(max_length=125, upload_to='organization/%Y/%m', verbose_name='机构图标')),
                ('fav_nums', models.IntegerField(verbose_name='收藏数')),
                ('org_click_nums', models.IntegerField(verbose_name='点击数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='教师名称')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('tea_icon', models.ImageField(max_length=125, upload_to='organization/%Y/%m', verbose_name='教师图标')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('work_years', models.IntegerField(verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=20, verbose_name='在职公司')),
                ('work_position', models.CharField(max_length=20, verbose_name='在职岗位')),
                ('work_points', models.CharField(max_length=100, verbose_name='教学特点')),
                ('fav_nums', models.IntegerField(verbose_name='收藏数')),
                ('tea_click_nums', models.IntegerField(verbose_name='点击数')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.Organization', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]
