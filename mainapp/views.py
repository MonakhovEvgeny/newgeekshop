from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'title': 'GeekShop',
        'categorys': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)
