# Generated by Django 4.2.5 on 2023-10-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0018_booking_dropoff_latitude_booking_dropoff_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_distance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
