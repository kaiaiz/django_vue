# encoding=utf-8
"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin

from django.conf.urls import url, include
# from django.contrib import admin
from xadmin.plugins import xversion
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from .settings import MEDIA_ROOT

xversion.register_models()
xadmin.autodiscover()

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # goods list
    url(r'^goods/', include('goods.urls', namespace="goods")),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^trade/', include('trade.urls', namespace="trade")),
    url(r'^user_operation/', include('user_operation.urls', namespace="user-operations")),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls')),
    # drt
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^docs/', include_docs_urls(title=u"超市")),
]
