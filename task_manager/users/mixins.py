from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _

class LoginRequired(LoginRequiredMixin):
    login_url = 'login'
    permission_denied_message = _("Please authorize to proceed!")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, self.permission_denied_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class CheckUserMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user == self.get_object():
            return True
        else:
            messages.error(self.request, _("You don't have access to edit other users profile."))
            return False

    def handle_no_permission(self):
        return redirect('users_index')





