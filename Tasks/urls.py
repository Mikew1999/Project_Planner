from django.urls import path
from . import views

app_name = "Tasks"

urlpatterns = [
    path("return_task_lists", views.return_task_lists, name="return_task_lists"),
    path("edit_task_list", views.edit_task_list, name="edit_task_list"),
    path("return_tasks", views.return_tasks, name="return_tasks")
]
