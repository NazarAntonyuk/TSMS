# Generated by Django 5.0.4 on 2024-05-19 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditorium', '0003_remove_equipmentinauditorium_non_current_asset'),
        ('non_current_asset', '0008_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinauditorium',
            name='non_current_asset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='non_current_asset.noncurrentasset', verbose_name='Необоротний актив'),
        ),
    ]
