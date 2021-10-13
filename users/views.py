from django.shortcuts import render

from users.forms import UserLoginForm


def login(request):
    form = UserLoginForm
    content = {
        'title': 'Geekshop - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', content)

def register(request):
    content = {
        'title': 'Geekshop - Регистрация'
    }
    return render(request, 'users/register.html', content)

