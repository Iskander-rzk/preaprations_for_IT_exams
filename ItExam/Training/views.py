from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h2>Main page<h2>")


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
