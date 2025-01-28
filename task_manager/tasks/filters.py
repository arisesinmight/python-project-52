import django_filters
from django import forms
from task_manager.tasks.models import Task

class TaskFilter(django_filters.FilterSet):
    only_users_tasks = django_filters.BooleanFilter(
        label='Only your tasks',
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
