# Generated by Django 5.0.4 on 2024-04-21 18:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalAppeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_appeals', models.CharField(max_length=255)),
                ('problem_aud', models.CharField(max_length=255)),
                ('description_problem', models.TextField()),
                ('contact_name', models.CharField(max_length=255)),
                ('tel_number', models.CharField(max_length=255)),
                ('date_appeals', models.DateField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]