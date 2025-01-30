from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _

from task_manager.statuses.models import Status


class StatusForm(ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Name')})
    )
    class Meta:
        model = Status
        fields = ['name']