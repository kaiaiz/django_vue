#encoding=utf-8

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'register', views.UserViewset, base_name="register")
urlpatterns = [
    url(r'^', include(router.urls)),
]
