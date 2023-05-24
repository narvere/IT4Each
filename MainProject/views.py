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

def register(request):
    return render(request, 'auth/register.html')
    
    
def login(request):
    """from django.utils.translation import activate, get_language
    from django.http import HttpResponse
    from django.shortcuts import render

    def login(request):
        user_language = 'et'
        activate(user_language)
        request.session['django_language'] = user_language
    """    
    #from django.conf import settings
    #from django.http import HttpResponse
    #from django.shortcuts import render
    from django.utils.translation import gettext as _


    #if settings.LANGUAGE_COOKIE_NAME in request.session:
    #    del request.session[settings.LANGUAGE_COOKIE_NAME]
    
    name = _('Homapege')
    
    context = {'name': name}
          
    
    return render(request, 'auth/login.html', context=context)

    
    
#def my_view(request):
#    output = _("Welcome to my site.")
#    return HttpResponse(output)


"""

class BaseView(View):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        contact = _('Контакт')
        context = {'contact': contact}
        return context
        
        """
def cont(request):
    contact = _('Контакт')
    context = {'contact': contact}
    return render(request, 'base.html', context=context)