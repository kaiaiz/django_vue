# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 13:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(default='', max_length=100, verbose_name='\u533a\u57df')),
                ('address', models.CharField(default='', max_length=100, verbose_name='\u8be6\u7ec6\u5730\u5740')),
                ('singer_name', models.CharField(default='', max_length=100, verbose_name='\u7b7e\u6536\u4eba')),
                ('singer_mobile', models.CharField(default='', max_length=100, verbose_name='\u7b7e\u6536\u7535\u8bdd')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6536\u83b7\u5730\u5740',
                'verbose_name_plural': '\u6536\u83b7\u5730\u5740',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6536\u85cf',
                'verbose_name_plural': '\u7528\u6237\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='UserLeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_type', models.CharField(choices=[(1, '\u7559\u8a00'), (2, '\u6295\u8bc9'), (3, '\u8be2\u95ee'), (4, '\u552e\u540e'), (5, '\u6c42\u8d2d')], default=1, help_text='\u7559\u8a00\u7c7b\u522b', max_length=2, verbose_name='\u7559\u8a00\u7c7b\u578b')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='\u7559\u8a00\u4e3b\u9898')),
                ('message', models.TextField(default='', verbose_name='\u7559\u8a00')),
                ('file', models.FileField(help_text='\u4e0a\u4f20\u7684\u6587\u4ef6', upload_to='', verbose_name='\u4e0a\u4f20\u7684\u6587\u4ef6')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7559\u8a00',
                'verbose_name_plural': '\u7528\u6237\u7559\u8a00',
            },
        ),
    ]