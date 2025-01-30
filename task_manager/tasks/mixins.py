from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class CheckAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        else:
            messages.warning(self.request, self.permission_denied_message)
            return False

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            return redirect(self.permission_denied_url)
        return (super(UserPassesTestMixin, self).
                dispatch(request, *args, **kwargs))











