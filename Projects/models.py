from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=55)
    color = models.CharField(max_length=55)

    class Meta:
        db_table = 'statuses'


class Project(models.Model):
    name = models.CharField(max_length=125)
    descr = models.TextField()
    start_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'projects'


class ProjectUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_users'
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'project_id'], name='unique_project_user')
        ]