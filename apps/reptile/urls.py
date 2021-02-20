from django.urls import path
from reptile import views


urlpatterns = [
    path('slogan/', views.SloganView.as_view()),

]
