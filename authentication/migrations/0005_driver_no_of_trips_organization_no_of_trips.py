# Generated by Django 5.1 on 2024-09-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_driver_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='no_of_trips',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='organization',
            name='no_of_trips',
            field=models.IntegerField(default=0),
        ),
    ]