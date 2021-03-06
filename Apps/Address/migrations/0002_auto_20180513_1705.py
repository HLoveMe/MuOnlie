# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-13 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='Address.Province', verbose_name='州/省/直辖市'),
        ),
        migrations.AddField(
            model_name='province',
            name='country',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='Address.Country', verbose_name='国家'),
        ),
        migrations.AddField(
            model_name='town',
            name='city',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='Address.Province', verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='town',
            name='desc',
            field=models.TextField(default='', verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='village',
            name='desc',
            field=models.TextField(default='', verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='village',
            name='town',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='Address.Province', verbose_name='镇'),
        ),
    ]
