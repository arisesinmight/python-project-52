from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class User(AbstractUser):

    def get_absolute_url(self):
        return reverse('users_index')

    def __str__(self):
        return self.get_full_name()
