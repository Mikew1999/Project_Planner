from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path("login/", views.login, name="login"),
]