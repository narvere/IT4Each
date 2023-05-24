from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.views import View


# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def detail(request):
    return render(request, 'detail.html')


def shop(request):
    return render(request, 'shop.html')


def cont(request):
    contact = _('Контакт')
    context = {'contact': contact}
    return render(request, 'base.html', context=context)
