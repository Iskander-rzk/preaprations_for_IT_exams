from django.shortcuts import render



def index(request):
    return render(request, 'project/index.html')  # Главная страница


def login(request):
    return render(request, "project/login.html") # О нас

def register(request):
    return render(request, "project/register.html") # О нас

