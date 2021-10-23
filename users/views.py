from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from baskets.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    content = {
        'title': 'Geekshop - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', content)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegisterForm()
    content = {
        'title': 'Geekshop - Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.error(request, 'Профиль сохранен')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            messages.error(request, 'Профиль не сохранен')
    total_sum = 0
    total_quantiti = 0
    baskets = Basket.objects.filter(user=request.user)
    for basket in baskets:
        total_quantiti += basket.quantiti
        total_sum += basket.sum()

    context = {
        'title': 'Geekshop - Профайл',
        'form': UserProfileForm(instance=request.user),
        'baskets': Basket.objects.filter(user=request.user),
        'total_quantiti': total_quantiti,
        'total_sum': total_sum,
    }
    return render(request, 'users/profile.html', context)
