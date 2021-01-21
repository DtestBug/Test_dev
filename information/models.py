from django.db import models
from utils.base_model import BaseModels


class InformationModels(BaseModels):
    consumables = models.TextField(verbose_name='consumables', help_text='消耗品', max_length=100)


    class Meta:
        db_table = 'information_table'
        verbose_name = '支出信息表'

        def __str__(self):
            pass
            # return f'<{self.name}>'
