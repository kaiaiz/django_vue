# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-24 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20180117_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_mount',
            field=models.FloatField(default=0.0, verbose_name='\u8ba2\u5355\u603b\u989d'),
        ),
    ]