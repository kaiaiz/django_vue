# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

from .serializers import UserRegSerializer


User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义后台验证，支持邮件
    """
    def authenticate(self, username=None, password=None,
                     **kwargs):
        try:
            user = User.objects.get(Q(username=username)
                                    |Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()



