# Generated by Django 5.0.4 on 2024-05-20 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal_appeals', '0006_journalappeals_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JournalAppeals',
        ),
    ]