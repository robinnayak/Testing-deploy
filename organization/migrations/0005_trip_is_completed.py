# Generated by Django 5.1 on 2024-08-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_alter_trip_organization_alter_trip_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
