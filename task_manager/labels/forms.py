from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _

from task_manager.labels.models import Label


class LabelForm(ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Name')})
    )
    class Meta:
        model = Label
        fields = ['name']