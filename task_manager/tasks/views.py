from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.mixins import LoginRequired
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.mixins import CheckAuthorMixin
from task_manager.tasks.models import Task


class TasksIndexView(LoginRequired, FilterView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/tasks_index.html'
    filterset_class = TaskFilter


class TaskView(LoginRequired, DetailView):
    model = Task
    template_name = 'tasks/task_details.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequired, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    template_name = 'tasks/task_create.html'
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        self.object = form.save()
        return super().form_valid(form)


class TaskUpdateView(LoginRequired, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    template_name = 'tasks/task_update.html'
    success_message = _('Task successfully updated')


class TaskDeleteView(LoginRequired, CheckAuthorMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks_index')
    template_name = 'tasks/task_delete.html'
    success_message = _('Task successfully removed')
    permission_denied_message = _("You don't have access for deleting other authors task.")
    permission_denied_url = 'tasks_index'
