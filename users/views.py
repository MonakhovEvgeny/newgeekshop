from django.shortcuts import render

def login(request):
    content = {
        'title': 'Geekshop - Авторизация'
    }
    return render(request, 'users/login.html', content)

def register(request):
    content = {
        'title': 'Geekshop - Регистрация'
    }
    return render(request, 'users/register.html', content)

