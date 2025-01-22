from django import forms
from django.forms import ModelForm
from task_manager.labels.models import Label
from django.utils.translation import gettext as _

class LabelForm(ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Name')})
    )
    class Meta:
        model = Label
        fields = ['name']