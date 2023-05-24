from MainProject import views
from django.urls import path


urlpatterns = [
    #path('', views.index, name='index'),
    #path('contact/', views.contact, name='contact_url'),
    #path('cart/', views.cart, name='cart'),
    #path('checkout/', views.checkout, name='checkout'),
    #path('detail/', views.detail, name='detail'),
    #path('shop/', views.shop, name='shop'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]