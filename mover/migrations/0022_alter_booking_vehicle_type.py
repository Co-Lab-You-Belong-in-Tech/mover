# Generated by Django 4.2.6 on 2023-10-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0021_customuser_address_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='vehicle_type',
            field=models.CharField(choices=[('SUV', 'SUV'), ('MiniVan', 'MiniVan'), ('Cargo Van', 'Cargo Van'), ('Pickup Truck', 'Pickup Truck')], default='Pickup Truck', max_length=50),
        ),
    ]
