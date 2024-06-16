from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'project/index.html')  # Главная страница


def about(request):
    return HttpResponse("<h4>About</h4>") # О нас