from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from task_manager.users.models import User
from task_manager.users.forms import UserForm
from django.urls import reverse_lazy
from task_manager.users.mixins import LoginRequired



class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_superuser=False)
        return render(request, 'users/index.html', context={'users': users})


class UserCreateView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('greeting')# сменить на login
    template_name = 'users/create.html'


class UserUpdateView(LoginRequired, UpdateView):
    form_class = UserForm
    success_url = reverse_lazy('greeting')
    template_name = 'users/update.html'

    def get_object(self, queryset=None):
        return self.request.user  #выбирает себя, надо ограничить остальных



class UserDeleteView(LoginRequired, DeleteView):
    model = User
    success_url = reverse_lazy('greeting')
    template_name = 'users/delete.html'
