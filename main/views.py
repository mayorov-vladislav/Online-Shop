from django.http import HttpResponse
from django.shortcuts import render
from goods.models import *

# Create your views here.
def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему этот магазин такой классный, и хорошие товары.'
    }

    return render(request, 'main/about.html', context)


def custom_404(request, exception):
    return render(request, 'templates/404.html', {}, status=404)

def custom_500(request):
    return render(request, '505.html', status=500)