from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label, Labeling
from task_manager.mixins import LoginRequired


class LabelsIndexView(LoginRequired, View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels/labels_index.html', context={'labels': labels})


class LabelCreateView(LoginRequired, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    template_name = 'labels/label_create.html'
    success_message = _('Label successfully created')


class LabelUpdateView(LoginRequired, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    template_name = 'labels/label_update.html'
    success_message = _('Label successfully updated')


class LabelDeleteView(LoginRequired, DeleteView):
    model = Label
    success_url = reverse_lazy('labels_index')
    template_name = 'labels/label_delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.warning(self.request, _("Unable to label that's on task."))
            return redirect('labels_index')
        labeling = Labeling.objects.filter(label=self.object.pk)
        labeling.delete()
        messages.success(self.request, _('Label successfully removed'))
        return self.delete(request, *args, **kwargs)