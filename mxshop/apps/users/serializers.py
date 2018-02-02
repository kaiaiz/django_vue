# encoding=utf-8

import pytz

from datetime import datetime
from datetime import timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import VerifyCode

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True,
                                 max_length=4, min_length=4)
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message="用户已存在le")])
    password = serializers.CharField(
        style={'input_type': 'password'},
        label='密码',
        write_only=True
    )

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            five_mintes_ago = five_mintes_ago.replace(tzinfo=pytz.timezone('UTC'))

            if five_mintes_ago < last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "password")