from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'auth/register.html')


def login_user(request):
    """from django.utils.translation import activate, get_language
    from django.http import HttpResponse
    from django.shortcuts import render

    def login(request):
        user_language = 'et'
        activate(user_language)
        request.session['django_language'] = user_language
    """
    # from django.conf import settings
    # from django.http import HttpResponse
    # from django.shortcuts import render
    from django.utils.translation import gettext as _

    # if settings.LANGUAGE_COOKIE_NAME in request.session:
    #    del request.session[settings.LANGUAGE_COOKIE_NAME]

    name = _('Homapege')

    context = {'name': name}

    return render(request, 'auth/login.html', context=context)


# def my_view(request):
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


def logout_user():
    pass
