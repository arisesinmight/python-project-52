import django_filters
from django import forms
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label=_('Status'),
        queryset=Status.objects.all(),
    )
    executor = django_filters.ModelChoiceFilter(
        label=_('Executor'),
        queryset=User.objects.filter(is_superuser=False),
    )
    labels = django_filters.ModelChoiceFilter(
        label=_('Label'),
        queryset=Label.objects.all(),
    )
    only_users_tasks = django_filters.BooleanFilter(
        label=_('Only your tasks'),
        method='is_users_task',
        widget=forms.CheckboxInput
    )

    def is_users_task(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
