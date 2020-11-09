from django.urls import path, re_path
from register import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path(r'userdatas/', views.UserDatasView.as_view()),

    path(r'userdata/<username>', views.UserDataView.as_view()),

]