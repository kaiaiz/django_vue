# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    user
    """
    gender_choices = (
        ("male", u"男"),
        ("female", u"女"),
    )
    name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=u"姓名")
    birthday = models.DateField(
        null=True, blank=True, verbose_name=u"出生年月")
    mobile = models.CharField(
        null=True, blank=True, max_length=11, verbose_name=u"手机号码",
        help_text="手机号码")
    gender = models.CharField(max_length=6, choices=gender_choices,
        default="male", verbose_name=u"性别")
    email = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=u"邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证麻
    """
    code = models.CharField(
        max_length=8, verbose_name=u"验证码")
    mobile = models.CharField(
        max_length=11, verbose_name=u"电话号码")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
