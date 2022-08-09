from django.urls import path
from app import views

urlpatterns = [
    path('upload/', views.upload_data, name='upload'),
]