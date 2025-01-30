from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from task_manager.users.models import User
from task_manager.users.forms import UserCreateForm, UserUpdateForm
from django.urls import reverse_lazy
from task_manager.users.mixins import CheckUserMixin
from task_manager.mixins import LoginRequired
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_superuser=False)
        return render(request, 'users/users_index.html', context={'users': users})


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/user_create.html'
    success_message = _("You've successfully signed up")


class UserUpdateView(LoginRequired, CheckUserMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users_index')
    template_name = 'users/user_update.html'
    success_message = _('You are successfully updated your data')
    permission_denied_message = _("You don't have access for editing other users profile.")
    permission_denied_url = 'users_index'


class UserDeleteView(LoginRequired, CheckUserMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users_index')
    template_name = 'users/user_delete.html'
    permission_denied_message = _("You don't have access for deleting other users profile.")
    permission_denied_url = 'users_index'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.got_tasks.exists() or self.object.created_tasks.exists():
            messages.warning(self.request, _("Unable to delete user that's in work."))
            return redirect('users_index')
        messages.info(self.request, _("You've deleted your profile"))
        return self.delete(request, *args, **kwargs)
