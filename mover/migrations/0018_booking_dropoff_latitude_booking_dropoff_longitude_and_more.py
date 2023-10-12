# Generated by Django 4.2.5 on 2023-10-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0017_vehicle_vehicle_type_delete_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='dropoff_latitude',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='dropoff_longitude',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_latitude',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_longitude',
            field=models.CharField(max_length=300, null=True),
        ),
    ]