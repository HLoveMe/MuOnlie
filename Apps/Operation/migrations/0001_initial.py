# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-13 06:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course', '0002_course_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('course', models.CharField(max_length=25, verbose_name='课程名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户询问',
                'verbose_name_plural': '用户询问',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course', verbose_name='课程')),
                ('superUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='super_set', to=settings.AUTH_USER_MODEL, verbose_name='@的用户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户课程',
                'verbose_name_plural': '用户课程',
            },
        ),
        migrations.CreateModel(
            name='UserCourseVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(default=0, verbose_name='已经学习时长')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.LessonVideo', verbose_name='学习视频')),
            ],
            options={
                'verbose_name': '学习时长',
                'verbose_name_plural': '学习时长',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='收藏对象ID')),
                ('fav_type', models.IntegerField(choices=[(1, '课程'), (2, '机构'), (3, '教师')], verbose_name='收藏类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='用户')),
                ('content', models.CharField(max_length=200, verbose_name='消息')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否已读')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
    ]
