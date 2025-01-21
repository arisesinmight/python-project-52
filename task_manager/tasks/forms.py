from django import forms
from django.forms import ModelForm
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from django.utils.translation import gettext as _

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
        label=_('Executioner'),
        queryset=User.objects.filter(is_superuser=False)
    )
    labels = forms.CharField(  #MultipleChoiceField(choises=(https://metanit.com/python/django/4.2.php)
        label=_('Labels'),
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('Labels')})
    )
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']