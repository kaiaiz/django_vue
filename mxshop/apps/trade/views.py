# encoding=utf-8
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication)
from django_filters.rest_framework import DjangoFilterBackend

from .models import ShoppingCart, OrderInfo, OrderGoods
from .serializers import (ShoppingCartSerializer,
                          ShoppingCartDetailSerializer,
                          OrderSerializer)
from utils.permissions import IsOwnerOrReadOnly


class ShoppingCartViewset(viewsets.ModelViewSet):
    """
    购物车功能
    list:
        获取购物车详情
    create:
        创建购物车
    update:
        更改购物车
    delete:
        删除购物车
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = ShoppingCartSerializer
    authentication_classes = (TokenAuthentication,
                              SessionAuthentication)
    filter_backends = (DjangoFilterBackend,)
    lookup_field = "goods_id"

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return ShoppingCartDetailSerializer
        else:
            return ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class OrderViewset(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    订单管理
    list:
        订单列表
    create:
        订单创建
    delete:
        订单删除
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,
                              SessionAuthentication)
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.nums = shop_cart.good_nums
            order_goods.order = order
            order_goods.save()

            shop_cart.delete

        return order



