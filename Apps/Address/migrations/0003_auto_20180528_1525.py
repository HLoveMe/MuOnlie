# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-28 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0002_auto_20180513_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '城市', 'verbose_name_plural': '城市'},
        ),
    ]
