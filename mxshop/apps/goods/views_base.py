#encoding=utf-8

import json

from django.views.generic.base import View
from django.http import HttpResponse

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表的展示
        """
        goods = Goods.objects.all()[:10]

        from django.core import serializers
        from django.http import JsonResponse
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)




