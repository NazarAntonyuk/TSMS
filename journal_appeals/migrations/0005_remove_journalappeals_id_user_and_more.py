# Generated by Django 5.0.4 on 2024-05-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_appeals', '0004_alter_journalappeals_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalappeals',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='journalappeals',
            name='number_appeals',
        ),
        migrations.AlterField(
            model_name='journalappeals',
            name='contact_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='journalappeals',
            name='date_appeals',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journalappeals',
            name='description_problem',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journalappeals',
            name='problem_aud',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='journalappeals',
            name='tel_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
