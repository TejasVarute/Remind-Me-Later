from django.contrib import admin
from .models import Reminder, PastReminder

# Register your models here.
admin.site.register(Reminder)
admin.site.register(PastReminder)