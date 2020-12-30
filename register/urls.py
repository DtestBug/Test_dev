from django.urls import path
from register import views
from rest_framework_jwt.views import obtain_jwt_token  # 登录类视图

urlpatterns = [
    path('login/', obtain_jwt_token),  # 登录 drf自带登录系统obtain_jwt_token
    path('register/', views.RegisterView.as_view()),
    path(r'userdatas/', views.UserDatasView.as_view()),
    path(r'userdata/<username>', views.UserDataView.as_view()),

]
























