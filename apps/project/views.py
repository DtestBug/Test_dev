from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ProjectSerializers
from .models import Project

# Create your views here.
"""
1. from rest_framework import viewsets  viewsets:数据删改查，多条查询，修改，增加
2. from rest_framework import permissions  permissions:用户权限
"""


class ProjectViewSet(viewsets.ModelViewSet):
    # 获取项目模板中的所有信息
    queryset = Project.objects.all()
    # 序列化程序类：项目序列化
    serializer_class = ProjectSerializers
    # 用户权限,需要使用中括号
    """
    permissions.AllowAny: 不需要登录就有任意权限
    permissions.IsAuthenticated: 只要登录就有任意权限
    permissions.IsAdminUser: 只有管理员账号登录就有任意权限
    """
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        return self.serializer_class

