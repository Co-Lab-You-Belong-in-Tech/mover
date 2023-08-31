# Generated by Django 4.2.4 on 2023-08-31 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='location',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='car_photo',
        ),
        migrations.CreateModel(
            name='VehiclePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('vehicle_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mover.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.IntegerField(help_text='Weight in KG')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
