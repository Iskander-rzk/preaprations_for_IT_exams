from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'), # Главная страница
    path('login/', views.login, name='login'), # О нас
    path('register/', views.register, name='register'),
]