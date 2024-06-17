from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index), # Главная страница
    path('login', views.login), # О нас
    path('register', views.register),
]