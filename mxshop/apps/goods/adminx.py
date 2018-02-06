import xadmin

from .models import (Goods, GoodsCategory, GoodsCategoryBrand, Banner,
                     GoodsImage)


class GoodsAdmin(object):
    list_display = ["name", "click_num", "sold_num", "fav_num",
                    "goods_sn", "market_price", "shop_price", "goods_brief",
                    "goods_desc", "is_new", "is_hot"]
    search_fields = ["name"]
    list_editable = ["is_hot"]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "market_price",
                   "shop_price", "is_new", "is_hot"]
    #style_fields = {}

    #class GoodsImagesInline(object):
    #    models = GoodsImage
    #    exclude = ["add_time"]
    #    extra = 1
    #    style = 'tab'

    #inlines = [GoodsImagesInline]


class GoodsCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ["name"]


class GoodsImageAdmin(object):
    list_display = ["goods", "image", "add_time"]
    list_filter = ["goods", ]
    search_fields = ["goods", "add_time"]


class GoodsBrandAdmin(object):
    list_display = ["category", "image", "name", "desc"]

    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context


class BannerGoodsAdmin(object):
    list_display = ["goods", "image", "index"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
