from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index), # Главная страница
    path('about-us', views.about), # О нас
]