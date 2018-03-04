#encoding=utf-8
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (GoodsSerializer, CategorySerializer,
                          BannerSerializer, IndexCategorySerializer)
from .models import (Goods, GoodsCategory, Banner)
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """
    list of goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    filter_class = GoodsFilter
    pagination_class = GoodsPagination
    #authentication_classes = (TokenAuthentication,)
    search_fields = ("name", "goods_brief", "goods_desc", "is_hot")
    ordering_fields = ('sold_num', 'shop_price')
    #filter_fields = ('category', 'name', 'shop_price')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    List:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)


class BannerViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    List:
        首页轮播图显示
    """
    queryset = Banner.objects.all().order_by("-index")
    serializer_class = BannerSerializer
    filter_backends = (DjangoFilterBackend,)


class IndexCategoryViewSet(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    """
    List:
        商品分类显示
    """
    queryset = GoodsCategory.objects.filter(is_tab=True)
    serializer_class = IndexCategorySerializer
    filter_backends = (DjangoFilterBackend,)
