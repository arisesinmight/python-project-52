from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskForm(ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Name')})
    )
    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={'placeholder': _('Description')})
    )
    status = forms.ModelChoiceField(
        label=_('Status'),
        queryset=Status.objects.all()
    )
    executor = forms.ModelChoiceField(
        label=_('Executor'),
        queryset=User.objects.filter(is_superuser=False)
    )
    labels = forms.ModelMultipleChoiceField(
        label=_('Labels'),
        queryset=Label.objects.all(),
        required=False
    )
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']