# Generated by Django 4.2.4 on 2023-09-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dropoff_location',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pickup_location',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='drivers_license',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='drivers_license_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fixed_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='hourly_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='license_expiration',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='license_state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='license_zipcode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profie_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rate_of_service',
            field=models.CharField(blank=True, choices=[('FX', 'Fixed'), ('HR', 'Hourly')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('driver', 'Driver'), ('customer', 'Customer')], max_length=10, null=True),
        ),
    ]
