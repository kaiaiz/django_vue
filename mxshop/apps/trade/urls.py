#encoding=utf-8
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
#用户购物车
router.register(r'shopcart', views.ShoppingCartViewset, base_name='shopcart')
#用户订单
router.register(r'shoporder', views.OrderViewset, base_name='order')

urlpatterns = [
    url(r'^', include(router.urls)),
]
