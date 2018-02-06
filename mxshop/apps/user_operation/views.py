# encoding=utf-8
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from .serializers import (UserFavSerializer,
                          UserFavDetailSerializer,
                          LeavingMessageSerializer,
                          UserAddressSerializer)
from .models import UserFav, UserLeavingMessage, UserAddress
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewset(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否收藏
    create:
        收藏商品
    delete:
        删除收藏
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer
    filter_backends = (DjangoFilterBackend,)
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer
        return UserFavSerializer


class LeavingMessageViewset(mixins.ListModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言
    """
    serializer_class = LeavingMessageSerializer
    filter_backends = (DjangoFilterBackend,)
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class UserAddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取用户地址
    create:
        添加收货地址
    update:
        更新收获地址
    delete:
        删除收获地址
    """
    serializer_class = UserAddressSerializer
    filter_backends = (DjangoFilterBackend,)
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
