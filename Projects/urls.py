from django.urls import path
from . import views

app_name = "Projects"

urlpatterns = [
    path("", views.index, name="index"),
    path("get_projects", views.get_projects, name="get_projects"),
    path("edit_project_details", views.edit_project_details, name="edit_project_details")
]