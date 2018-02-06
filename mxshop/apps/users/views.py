# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin,
                                   UpdateModelMixin,
                                   RetrieveModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication)
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserRegSerializer, UserDetailSerializer


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


class UserViewset(CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    用户详情页
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication,)
    filter_backends = (DjangoFilterBackend,)
    #permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == "retrieve":
            return [IsAuthenticated()]
        elif self.action == 'create':
            return []
        return []

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer
        return UserDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_object(self):
        return self.request.user





