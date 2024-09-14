# Generated by Django 5.1 on 2024-08-28 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_passenger'),
        ('organization', '0003_trip_last_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='authentication.organization'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='vehicle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='organization.vehicle'),
        ),
    ]