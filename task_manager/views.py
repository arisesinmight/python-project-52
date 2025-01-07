from django.shortcuts import render, get_object_or_404
from django.views import View
from task_manager.models import User


class HelloView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'greetings.html')


class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users_index.html', context={'users': users})