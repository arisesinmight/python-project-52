from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy



class HelloView(TemplateView):
    template_name = 'greetings.html'



class TMLogoutView(SuccessMessageMixin, LogoutView):
    success_message = _('You are logged out')
    success_url = reverse_lazy('greeting')

class TMLoginView(SuccessMessageMixin, LoginView):
    success_message = _('You are logged in')
    success_url = reverse_lazy('greeting')