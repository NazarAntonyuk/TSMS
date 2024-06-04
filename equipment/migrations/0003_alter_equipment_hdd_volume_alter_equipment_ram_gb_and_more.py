# Generated by Django 5.0.4 on 2024-05-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='hdd_volume',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Об'єм HDD"),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='ram_gb',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ОЗУ (GB)'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='router_speed',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Швидкість маршрутизатора'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='ssd_volume',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Об'єм SSD"),
        ),
    ]
