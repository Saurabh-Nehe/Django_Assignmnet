from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):

    task_name = models.CharField(max_length = 50)
    description = models.CharField(max_length=100)
    modified_date = models.DateTimeField(default=timezone.now)
    status = models.TextField(default="Pending")
    deadline = models.DateTimeField()
    # id = models.AutoField(primary_key=True)

    
    def __str__(self):
        return self.task_name

