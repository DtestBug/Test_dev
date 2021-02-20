from rest_framework import serializers
from .models import Project


class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        # 使用项目模板
        model = Project

        # 更新时间字段不提供给前端
        exclude = ('update_time', )

