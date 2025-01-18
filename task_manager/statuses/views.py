from django.views import View
from django.shortcuts import render
from task_manager.statuses.models import Status
from django.views.generic import CreateView, UpdateView, DeleteView
from task_manager.statuses.forms import StatusForm
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import LoginRequired


class StatusesIndexView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, 'statuses/statuses_index.html', context={'statuses': statuses})


class StatusCreateView(LoginRequired, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    template_name = 'statuses/status_create.html'
    success_message = _('Status successfully created')


class StatusUpdateView(LoginRequired, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    template_name = 'statuses/status_update.html'
    success_message = _('Status successfully updated')


class StatusDeleteView(LoginRequired, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses_index')
    template_name = 'statuses/status_delete.html'
    success_message = _('Status successfully removed')
