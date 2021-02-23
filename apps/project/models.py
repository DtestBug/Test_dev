from django.db import models
from utils.base_model import BaseModels
# Create your models here.


"""
# 项目
1。unique=True  必须是唯一的
2.return self.name   将项目名返回，

"""


class Project(BaseModels):
    name = models.CharField(help_text="项目名", verbose_name="项目名", unique=True, max_length=200)
    leader = models.TextField(help_text="负责人", verbose_name="负责人")
    tester = models.TextField(help_text="测试人员", verbose_name="测试人员")
    programmer = models.TextField(help_text="开发人员", verbose_name="开发人员")
    desc = models.TextField(help_text="描述", verbose_name="描述")

    class Meta:
        db_table = "project"
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

