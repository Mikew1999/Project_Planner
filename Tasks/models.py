from django.db import models
from Projects.models import Project
from Projects.models import Status

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=55)
    color = models.CharField(max_length=55)
    descr = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'task_lists'


class Task(models.Model):
    name = models.CharField(max_length=55)
    descr = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'tasks'
