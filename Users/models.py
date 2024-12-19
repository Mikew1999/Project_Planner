from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=125, unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=18)
    last_login = models.DateTimeField()
    created_time = models.DateTimeField()
    deleted = models.BooleanField()
