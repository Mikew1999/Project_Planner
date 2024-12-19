from django.urls import path
from . import views

app_name = "Projects"

urlpatterns = [
    path("", views.index, name="index")
]