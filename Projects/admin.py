from django.contrib import admin

from .models import Project, ProjectUser, Status

admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(Status)
