from django.urls import path
from .views import reminder, old_reminder, page_not_found

app_name = "reminder"
urlpatterns = [
    path('remind', reminder, name='my_reminder'),
    path('old_remind', old_reminder, name='old_reminder'),
    path('404', page_not_found, name='404_error'),
]