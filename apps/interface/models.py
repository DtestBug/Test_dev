from utils.base_model import BaseModels
from django.db import models


class Interface(BaseModels):
    name = models.CharField(help_text="接口名称", verbose_name="接口名称", unique=True)
    project = models.ForeignKey(to='project.Project', on_delete=models.CASCADE, related_name="interface", help_text="所属项目")
    tester = models.CharField(help_text="测试人员", verbose_name="测试人员")
    desc = models.CharField(help_text="接口描述", verbose_name="接口描述")






