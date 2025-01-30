from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Labeling(models.Model):
    task = models.ForeignKey('tasks.Task', on_delete=models.SET_NULL, blank=True, null=True)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)