# encoding=utf-8
import time

from rest_framework import serializers

from .models import (ShoppingCart,
                     OrderInfo,
                     OrderGoods)
from goods.models import Goods
from goods.serializers import GoodsSerializer


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    good_nums = serializers.IntegerField(required=True, min_value=1,
                                         error_messages={
                                             "min_value": "商品数量不能小于1",
                                             "required": "请填写购买数量"
                                         })
    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all(),
                                               required=True)
    add_time = serializers.DateTimeField(read_only=True,
                                         format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ShoppingCart
        fields = ("user", "goods", "good_nums", "add_time")

    def create(self, validated_data):
        user = self.context['request'].user
        good_nums = validated_data["good_nums"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user,
                                              goods=goods)

        if existed:
            existed = existed[0]
            existed.good_nums += good_nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ShoppingCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = ShoppingCart
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.CharField(read_only=True)

    def generate_order_sn(self):
        from random import randint
        random_ins = randint(10, 99)
        order_sn = "{time_str}{userid}{ranstr}".format(
            time_str=time.strftime("%Y%m%d%H%M%S"),
            userid=self.context["request"].user.id,
            ranstr=random_ins
        )
        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"


