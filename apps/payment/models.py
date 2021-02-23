from django.db import models
from utils.base_model import BaseModels


class PaymentModels(BaseModels):
    buy_time = models.DateField(verbose_name='buy_time', help_text='购买时间', null=True)
    category = models.CharField(verbose_name='category', help_text='类别', max_length=50)
    product = models.CharField(verbose_name='product', help_text='消耗品', max_length=100)
    count = models.IntegerField(verbose_name='count', help_text='消耗数量')
    price = models.IntegerField(verbose_name='price', help_text='价格')
    use_time = models.IntegerField(verbose_name='use_time', help_text='使用时长')
    pet_name = models.ForeignKey('pets.PetsModels', on_delete=models.CASCADE, related_name='payment', help_text='所属宠物')

    class Meta:
        db_table = 'pets_consume'
        verbose_name = '宠物消耗品'

    def __str__(self):
        return self.pet_name
