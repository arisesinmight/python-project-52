from django.shortcuts import render, get_object_or_404
from django.views import View



class HelloView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'greetings.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        pass