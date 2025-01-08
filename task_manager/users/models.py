from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    def get_absolute_url(self):
        return reverse('users_index')

    def __str__(self):
        return self.get_full_name()

'''class User(models.Model):
    nickname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)'''