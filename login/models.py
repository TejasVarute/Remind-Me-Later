from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    
    def __str__(self):
        return self.username
    