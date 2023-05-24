from django.contrib import admin
from django.urls import path
from MainProject import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact_url'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/', views.detail, name='detail'),
    path('shop/', views.shop, name='shop'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
