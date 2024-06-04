# Generated by Django 5.0.4 on 2024-04-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_equipment', models.CharField(max_length=255, verbose_name='Тип обладнання')),
            ],
            options={
                'verbose_name_plural': 'Equipment Types',
                'db_table': 'equipment_type',
            },
        ),
    ]
