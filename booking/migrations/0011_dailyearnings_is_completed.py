# Generated by Django 5.1 on 2024-09-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_booking_trip_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyearnings',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
