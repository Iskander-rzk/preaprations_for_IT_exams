from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index), # Главная страница
    path('entrance', views.entrance), # О нас
]