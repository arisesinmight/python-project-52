from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class HelloView(TemplateView):
    template_name = 'greetings.html'



class TMLogoutView(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)


class TMLoginView(SuccessMessageMixin, LoginView):
    success_message = _('You are logged in')

