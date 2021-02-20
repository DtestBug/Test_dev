from django.urls import path
from payment import views
from rest_framework.routers import SimpleRouter


# 定义路由对象
router = SimpleRouter()
urlpatterns = [
    # 创建，list查询
    path('payment/', views.PaymentViewSet.as_view()),

]
urlpatterns += router.urls
