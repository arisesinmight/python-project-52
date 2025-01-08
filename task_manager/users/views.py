from django.shortcuts import render, get_object_or_404
from django.views import View
from task_manager.users.models import User


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_superuser=False)
        return render(request, 'users/index.html', context={'users': users})