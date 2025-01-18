from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from task_manager.users.models import User
from task_manager.users.forms import UserForm
from django.urls import reverse_lazy
from task_manager.users.mixins import CheckUserMixin
from task_manager.mixins import LoginRequired
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_superuser=False)
        return render(request, 'users/users_index.html', context={'users': users})


class UserCreateView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'users/user_create.html'


class UserUpdateView(LoginRequired, CheckUserMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_index')
    template_name = 'users/user_update.html'
    success_message = _('You are successfully updated your data')


class UserDeleteView(LoginRequired, CheckUserMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'users/user_delete.html'
    success_message = _("You've deleted your profile")

