from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label, Labeling




class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='on_task')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='got_tasks')
    labels = models.ManyToManyField(Label, through=Labeling)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


