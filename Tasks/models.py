from django.db import models
from Projects.models import Project

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=55)
    color = models.CharField(max_length=55)
    descr = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'task_lists'
