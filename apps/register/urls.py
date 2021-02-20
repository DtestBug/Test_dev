from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token  # 登录类视图

urlpatterns = [
    path('login/', obtain_jwt_token),  # 登录 drf自带登录系统obtain_jwt_token
    path(r'register/', views.RegisterView.as_view()),
    path(r'userdatas/', views.UserDatasView.as_view()),
    path(r'userdata/<username>', views.UserDataView.as_view()),

    path(r'register/<username>', views.UserView.as_view()),

]
























