from django.db import models
from utils.base_model import BaseModels


class PetsModels(BaseModels):
    name = models.CharField(verbose_name='宠物名', help_text='宠物名', max_length=10, unique=True)
    weight = models.TextField(verbose_name='体重', help_text='体重', max_length=3)
    age = models.TextField(verbose_name='出生时长', help_text='出生时长', max_length=3)
    varieties = models.TextField(verbose_name='品种', help_text='品种', max_length=50)
    color = models.TextField(verbose_name='颜色', help_text='颜色', max_length=20)

    class Meta:
        db_table = 'pets_data'
        verbose_name = '宠物信息表'
