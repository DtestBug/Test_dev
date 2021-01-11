from rest_framework import permissions
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from .serializers import PetSerializer
from .models import PetsModels


# GenericAPIView              请求
# GenericAPIView和APIView只支持对get,post,put,delete,patch等请求方法
# GenericAPIView为APIview的子类，拓展了过滤、查询、分页
# mixins.CreateModelMixin     创建数据
# mixins.ListModelMixin       list查询
class PetsViews(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericAPIView
                ):
    queryset = PetsModels.objects.all()
    serializer_class = PetSerializer
    # filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,排序引擎
    # filterset_fields = ['name', 'leader', 'id']  #过滤字段
    # ordering_fields = ['id', 'name']  # 排序引擎   示例：http://127.0.0.1:8000/index/projects/?ordering=id，id前面加-可以倒序
    # pagination_class = MyPagination  # 在视图中指定分页
    # authentication_classes = ['']  # authentication_classes在视图中指定权限，可以在列表中添加多个权限类
    # permission_classes = [permissions.IsAuthenticated]  # 视图中指定的权限优先级大于全局指定的权限

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# mixins.RetrieveModelMixin   单个查询
# mixins.UpdateModelMixin     更新数据
# mixins.DestroyModelMixin    删除数据
class PetsView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericAPIView
               ):
    queryset = PetsModels.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "name"  # 指定查询字段

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
