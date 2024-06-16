from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'project/index.html')  # Главная страница


def entrance(request):
    return render(request, "project/entrance.html") # О нас