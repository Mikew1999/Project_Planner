from django.contrib import admin

from .models import Project, ProjectUser, Status

admin.register(Project)
admin.register(ProjectUser)
admin.register(Status)
