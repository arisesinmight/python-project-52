from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from task_manager.mixins import LoginRequired
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusesIndexView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(
            request,
            'statuses/statuses_index.html',
            context={'statuses': statuses}
        )


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


class StatusDeleteView(LoginRequired, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses_index')
    template_name = 'statuses/status_delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.on_task.exists():
            messages.warning(
                self.request, _("Unable to delete status that's in use.")
            )
            return redirect('statuses_index')
        messages.success(self.request, _('Status successfully removed'))
        return self.delete(request, *args, **kwargs)

