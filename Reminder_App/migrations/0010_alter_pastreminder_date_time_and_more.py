# Generated by Django 5.2.3 on 2025-07-08 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder_App', '0009_alter_pastreminder_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastreminder',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 8, 16, 15, 58, 241072)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 8, 16, 15, 58, 240796)),
        ),
    ]
