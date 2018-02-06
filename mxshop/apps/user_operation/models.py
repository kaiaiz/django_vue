#encoding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods


User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(
        User, verbose_name=u"用户")
    goods = models.ForeignKey(
        Goods, verbose_name=u"商品",
        help_text=u"商品id")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name
#        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserLeavingMessage(models.Model):
    """
    用户留言信息
    """
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购"),
    )
    user = models.ForeignKey(
        User, verbose_name=u"用户")
    msg_type = models.CharField(
        default=1, max_length=2, choices=MESSAGE_CHOICES,
        verbose_name=u"留言类型", help_text="留言类别")
    subject = models.CharField(
        default="", max_length=100, verbose_name=u"留言主题")
    message = models.TextField(
        default="", verbose_name=u"留言")
    file = models.FileField(
        upload_to="message/images/", verbose_name=u"上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    用户收获地址
    """
    user = models.ForeignKey(
        User, verbose_name=u"用户")
    district = models.CharField(
        max_length=100, default="", verbose_name=u"区域")
    address = models.CharField(
        max_length=100, default="", verbose_name=u"详细地址")
    singer_name = models.CharField(
        max_length=100, default="", verbose_name=u"签收人")
    singer_mobile = models.CharField(
        max_length=100, default="", verbose_name=u"签收电话")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"收获地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


