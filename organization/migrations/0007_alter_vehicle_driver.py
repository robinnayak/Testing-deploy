# Generated by Django 5.1 on 2024-09-11 02:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_driver_license_number'),
        ('organization', '0006_alter_trip_from_location_alter_trip_to_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='vehicle_driver', to='authentication.driver'),
        ),
    ]