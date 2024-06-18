from django.shortcuts import render, redirect
from .models import User1
from .forms import User
from django.contrib import messages



def index(request):
    return render(request, 'project/index.html')  # Главная страница


def login(request):
    if request.method == 'POST':
        form = User()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.check_user(username, password)
            if form.check_user():
                return redirect('project/index.html')
            else:
                messages.error(request, "Неверный логин или пароль.")
    return render(request, "project/login.html") # О нас


def register(request):
    return render(request, "project/register.html") # О нас

