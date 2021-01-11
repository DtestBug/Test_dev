from django.db import models


class BaseModels(models.Model):
    # 1.auto_now_add=True自增现在的时间
    # 2.auto_now
    # 3.primary_key唯一主键
    id = models.AutoField(verbose_name='id', primary_key=True, help_text='id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update_time', help_text='更新时间')

    class Meta:
        abstract = True  # 指定abstract为True时，在迁移时不创建表
