from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from task_manager.users.models import User
from task_manager.users.forms import SignUpForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_superuser=False)
        return render(request, 'users/index.html', context={'users': users})


class UserCreateView(CreateView):

    form_class = SignUpForm
    template_name = 'users/create.html'


class UserUpdateView(UpdateView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class UserDeleteView(DeleteView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
