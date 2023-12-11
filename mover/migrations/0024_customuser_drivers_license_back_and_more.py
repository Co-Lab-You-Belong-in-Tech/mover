# Generated by Django 4.2.6 on 2023-12-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0023_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='drivers_license_back',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='drivers_license_front',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='interior_vehicle_photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='service_type',
            field=models.CharField(choices=[('LOAD', 'Load'), ('UNLOAD', 'Unload'), ('BOTH', 'Both')], default='LOAD', max_length=100, null=True),
        ),
    ]
