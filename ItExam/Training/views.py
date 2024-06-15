from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
    return HttpResponse("<h2>Main page<h2>")


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Замените 'home' на URL вашей главной страницы
            else:
                form.add_error(None, "Invalid username or password")
    return render(request, 'login.html', {'form': form})




def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")


def about(rerquest, name, age):
    return HttpResponse(f""" 
    <h2>About user</h2>
    <p> Name: {name}</p>
    <p> Age: {age}</p>
    """)


def lol(request):
    text = """C'mon, let's go!
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠄⠒⠂⢀
   ⢀⠄⠄⠄⠄⠄⠄⠄⠄⢀⡀⠄⣰⣶⣦⡈
   ⠄⠄⠂⠄⠄⠄⠄⠄⠄⠄⣿⣖⣿⣷⣴⡄
   ⠄⠄⠄⠄⠁⠄⠄⠄⠄⣸⣿⣿⣿⠛⠩⠁
   ⠄⠄⠄⠄⠄⠄⣀⣤⣾⣿⣿⡏⠉⠄⠁
   ⠄⠄⢀⣴⣶⣿⣿⣿⣿⣿⡟⠺⡇⠄⢵⣤⣀
   ⠄⢠⣿⣿⣿⣿⣿⣿⣿⡏⠁⠄⣷⣀⠈⠙⠛⠑⠄
   ⠄⣼⣿⣿⣿⡇⠹⣿⣿⣿⡦⠄⠹⢿⡇⠄⠄⠄⠄
   ⠄⣿⣿⣿⣿⠁⢰⣤⣀⣀⣠⣔⢰⠄⠄⠄⠄⢀⡈
   ⢠⣿⣿⠟⠄⠄⢸⣿⣿⣿⣿⠏⢸⡆⠄⠐⠄⢸⣿⣌
   ⢸⣿⣿⡆⠄⠄⢸⣿⡿⢿⡤⠄⠈⠄⠄⢀⠄⢰⣿⣿⡄
   ⠈⢿⣿⣷⠄⠄⠄⣿⣷⣦⠄⠐⠄⠄⠄⠘⠄⠘⢿⣿⡇
   ⠄⠈⠻⣿⣇⠠⠄⢀⡉⠄⠄⠄⠄⠄⢀⡆⠄⠄⠘⣿⡇
   ⠄⠄⠄⠘⣿⣧⢀⣿⣿⢷⣶⣶⣶⣾⢟⣾⣄⠄⡴⣿⡀
   ⠄⠄⠄⠄⠘⣿⣧⣝⣿⣷⣝⢿⣿⠇⢸⣿⣿⡎⡡⠋⠄
   ⠄⠄⠄⠄⠄⣝⠛⠋⠁⣿⣿⡎⢠⣴⣾⣿⣿⣷⠄
   ⠄⠄⠄⠄⢠⣿⣷⣾⣿⣿⣿⠁⠘⢿⣿⣿⣿⣿⡄"""

    # Разделение текста на строки
    lines = text.split('\n')

    # Формирование HTTP-ответа с каждой строкой в качестве содержимого
    response = HttpResponse()
    for line in lines:
        response.write(line + '<br>')

    return response


def contact(request):
    return HttpResponse("<h2>Contacts<h2>")
