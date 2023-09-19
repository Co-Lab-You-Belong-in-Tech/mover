# Generated by Django 4.2.5 on 2023-09-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0004_remove_customuser_selected_item_booking_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='photo',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='booking',
            name='rate_type',
            field=models.CharField(choices=[('FX', 'Fixed'), ('HR', 'Hourly')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='service_type',
            field=models.CharField(choices=[('LOAD', 'Load'), ('UNLOAD', 'UnLoad'), ('BOTH', 'Both')], max_length=100, null=True),
        ),
    ]
