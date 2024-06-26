# Generated by Django 5.0.4 on 2024-04-18 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Процесор')),
                ('ram_gb', models.IntegerField(blank=True, null=True, verbose_name='ОЗУ (GB)')),
                ('ram_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип ОЗУ')),
                ('hdd_volume', models.IntegerField(blank=True, null=True, verbose_name="Об'єм HDD")),
                ('ssd_volume', models.IntegerField(blank=True, null=True, verbose_name="Об'єм SSD")),
                ('motherboard', models.CharField(blank=True, max_length=255, null=True, verbose_name='Материнська плата')),
                ('motherboard_socket', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сокет материнської плати')),
                ('power_supply', models.CharField(blank=True, max_length=255, null=True, verbose_name='БЖ')),
                ('operating_system', models.CharField(blank=True, max_length=255, null=True, verbose_name='Операційна система')),
                ('office_software', models.CharField(blank=True, max_length=255, null=True, verbose_name='Офісне ПЗ')),
                ('specialized_software', models.CharField(blank=True, max_length=255, null=True, verbose_name='Спеціалізоване ПЗ')),
                ('screen_diagonal', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Діагональ екрану')),
                ('screen_resolution', models.CharField(blank=True, max_length=255, null=True, verbose_name='Роздільна здатність екрану')),
                ('projector_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип проектора')),
                ('projector_resolution', models.CharField(blank=True, max_length=255, null=True, verbose_name='Роздільна здатність проектора')),
                ('router_speed', models.IntegerField(blank=True, null=True, verbose_name='Швидкість маршрутизатора')),
                ('ports_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кількість портів/занятих портів')),
                ('equipment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.equipmenttype', verbose_name='Тип обладнання')),
            ],
            options={
                'verbose_name_plural': 'Equipment',
                'db_table': 'equipment',
            },
        ),
    ]
