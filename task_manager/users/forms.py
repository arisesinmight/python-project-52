from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from django.utils.translation import gettext as _

from task_manager.users.models import User


class UserForm(ModelForm):
    first_name = forms.CharField(
        label=_('First_name'),
        widget=forms.TextInput(attrs={'placeholder': _('First_name')})
    )
    last_name = forms.CharField(
        label=_('Last_name'),
        widget=forms.TextInput(attrs={'placeholder': _('Last_name')})
    )
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'placeholder': _('Username')}),
        help_text=_(
            'Required field. No more than 150 characters. Only letters,\
             numbers and symbols @/./+/-/_.'
        )
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Password')}),
        help_text=_(
            'Your password should be at least 3 symbols long.'
        )
    )
    password2 = forms.CharField(
        label=_('Submit password'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Submit password')}),
        help_text=_(
            'Please enter your password again to confirm.'
        )
    )


class UserCreateForm(UserForm, UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class UserUpdateForm(UserForm, UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

