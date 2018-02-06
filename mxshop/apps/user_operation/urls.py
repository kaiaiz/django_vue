#encoding=utf-8
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
#用户收藏
router.register(r'user_fav', views.UserFavViewset, base_name='user-fav')
#用户留言
router.register(r'messages', views.LeavingMessageViewset,
                base_name='leaving-msg')
#用户收获地址
router.register(r'address', views.UserAddressViewset,
                base_name='address')
urlpatterns = [
    url(r'^', include(router.urls)),
]
