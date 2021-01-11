from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User


# class RegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class UserDataView(APIView):

    def get(self, request, username):
        if User.objects.filter(username=username).count() >= 1:  # 判断该查找出的数据存在于数据库
            email = User.objects.values('email').get(username=username)['email']  # 获取数据库内名字为xx的邮箱
            is_superuser = User.objects.values('is_superuser').get(username=username)['is_superuser']
            res = {
                'username': username,
                'email': email,
                'is_superuser': is_superuser
            }
            return Response(res, status=status.HTTP_200_OK)
        if User.objects.filter(username=username).count() == 0:  # 如果为0，说明数据不存在返回404
            data = {
                'result': 'no data found',
                'code': 0
            }
            return Response(data,status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('未知错误')


class UserDatasView(APIView):  # 获取数据库所有参数
    def get(self, request):
        datas = User.objects.values()
        return Response(datas)


