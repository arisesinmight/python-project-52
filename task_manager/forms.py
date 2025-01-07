from django.forms import ModelForm
from task_manager.models import User

class UserRegForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'password']