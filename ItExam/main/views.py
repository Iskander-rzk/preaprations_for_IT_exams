from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'project/index.html')  # Главная страница

@csrf_protect
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Замените на имя вашего URL для главной страницы
            else:
                messages.error(request, "Неверный логин или пароль.")
    else:
        form = LoginForm()
    return render(request, 'project/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно. Войдите в свой аккаунт.")
            return redirect('login')  # Перенаправление на страницу логина после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'project/register.html', {'form': form})
