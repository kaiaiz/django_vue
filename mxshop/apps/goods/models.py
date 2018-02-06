#encoding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, "一级目录"),
        (2, "二级目录"),
        (3, "三级目录"),
    )
    name = models.CharField(
        default="", max_length=30, verbose_name="类别名称")
    code = models.CharField(
        default="", max_length=30, verbose_name=u"类别编码",
        help_text="类别编码")
    desc = models.CharField(
        default="", max_length=300, verbose_name="类别描述",
        help_text="类目级别")
    category_type = models.IntegerField(
        choices=CATEGORY_TYPE, verbose_name=u"目录类型")
    parent_category = models.ForeignKey(
        "self", null=True, blank=True, verbose_name="父目录",
        related_name="sub_cat", help_text="父目录")
    is_tab = models.BooleanField(
        default=False, verbose_name=u"是否导航", help_text="是否导航")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    category = models.ForeignKey(
        GoodsCategory, null=True, blank=True,
        verbose_name=u"商品类别")
    name = models.CharField(
        default="", max_length=30, verbose_name=u"品牌名",
        help_text="品牌名")
    desc = models.TextField(
        default="", max_length=200, verbose_name=u"品牌描述",
        help_text=u"品牌描述")
    image = models.ImageField(
        max_length=200, upload_to="brand/images/")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(
        GoodsCategory, verbose_name=u"商品类别")
    goods_sn = models.CharField(
        max_length=50, default="", verbose_name=u"商品唯一货号")
    name = models.CharField(
        max_length=300, verbose_name=u"商品名")
    click_num = models.IntegerField(
        default=0, verbose_name=u"点击数")
    sold_num = models.IntegerField(
        default=0, verbose_name=u"商品销售量")
    fav_num = models.IntegerField(
        default=0, verbose_name=u"收藏数")
    market_price = models.FloatField(
        default=0, verbose_name=u"库存数")
    shop_price = models.FloatField(
        default=0, verbose_name="本店价格")
    goods_brief = models.TextField(
        max_length=50, verbose_name=u"商品简短描述")
    goods_desc = models.CharField(
        max_length=200, verbose_name=u"商品描述")
    ship_free = models.BooleanField(
        default=True, verbose_name=u"是否承担运费")
    goods_front_image = models.ImageField(
        upload_to="", null=True, blank=True, verbose_name=u"商品封面")
    is_new = models.BooleanField(
        default=False, verbose_name=u"是否新品")
    is_hot = models.BooleanField(
        default=False, verbose_name=u"是否热销")

    class Meta:
        verbose_name = u"商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(
        Goods, verbose_name=u"商品", related_name="images")
    image = models.ImageField(
        upload_to="", verbose_name=u"图片", null=True, blank=True)
    image_url = models.CharField(
        max_length=300, null=True, blank=True, verbose_name=u"图片url")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    轮播商品
    """
    goods = models.ForeignKey(
        Goods, verbose_name=u"商品")
    image = models.ImageField(
        upload_to="banner", verbose_name=u"轮播图片")
    index = models.IntegerField(
        default=0, verbose_name=u"轮播顺序")
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"首页商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
