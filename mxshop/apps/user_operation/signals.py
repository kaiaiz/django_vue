# encoding=utf-8
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserFav


@receiver(post_save, sender=UserFav)
def create_userfav(self, instance=None, created=False, **kwargs):
    # 实现用户收藏数的变更

    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()
