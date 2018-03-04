from django.db.models import Q
from rest_framework import serializers

from .models import (Goods, GoodsCategory, GoodsImage, Banner,
                     GoodsCategoryBrand)


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    class Meta:
        sub_cat = CategorySerializer3(many=True)
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new Goods instance, gave the validated_data
        """
        return Goods.objects.create(**validated_data)


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"


class IndexCategorySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = CategorySerializer2(many=True)

    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj)|
                                        Q(category__parent_category_id=obj)|
                                        Q(category__parent_category__parent_category_id=obj))
        goods_serializer = GoodsSerializer(all_goods, many=True)

        return goods_serializer.data

    class Meta:
        model = GoodsCategory
        fields = "__all__"
