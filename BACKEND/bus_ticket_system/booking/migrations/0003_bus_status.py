# Generated by Django 5.1.4 on 2025-01-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_destination_route_end_point_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available'), ('In Service', 'In Service'), ('Under Maintenance', 'Under Maintenance')], default='Available', max_length=20),
        ),
    ]
