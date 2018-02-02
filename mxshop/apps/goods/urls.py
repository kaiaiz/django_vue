from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views
from .filters import GoodsFilter


#Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'list', views.GoodsListViewSet)
router.register(r'category', views.CategoryViewSet, base_name="categorys")



urlpatterns = [
    url(r'^', include(router.urls)),
]
