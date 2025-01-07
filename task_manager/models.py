from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
