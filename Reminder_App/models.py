from django.db import models
from datetime import datetime
from login.models import UserData

class Reminder(models.Model):    
    date_time = models.DateTimeField(default=datetime.now())
    location = models.CharField(default="")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.message} @ {self.location} @ {self.date_time}'

class PastReminder(models.Model):
    date_time = models.DateTimeField(default=datetime.now())
    location = models.CharField(default="")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.message} @ {self.location} @ {self.date_time}'
    