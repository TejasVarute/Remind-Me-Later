from django.db import models
from django.core.exceptions import PermissionDenied

# Create your models here.
class UserData(models.Model):
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    
    def __str__(self):
        return self.username

class Developer(models.Model):
    first_name = models.CharField(max_length=10, default="Tejas")
    last_name = models.CharField(max_length=10, default="Varute")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'