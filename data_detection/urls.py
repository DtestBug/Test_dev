from django.urls import path
from data_detection import views


urlpatterns = [
    path('filetest/', views.FileUpload.as_view()),

]