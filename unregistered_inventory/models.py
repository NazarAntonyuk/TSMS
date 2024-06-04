# Create your models here.
from django.conf import settings
from django.db import models


class UnregisteredInventory(models.Model):
    name_unreg_aud = models.CharField(max_length=255, verbose_name="Назва", blank=True, null=True)
    quantity_unreg_aud = models.IntegerField(verbose_name="Кількість", blank=True, null=True)
    description_unreg_aud = models.TextField(verbose_name="Опис", blank=True, null=True)
    date_of_entry = models.DateField(verbose_name="Дата внесення", blank=True, null=True)
    note_unreg_aud = models.TextField(verbose_name="Примітка", blank=True, null=True)


    class Meta:
        verbose_name = "unregistered inventories"
        verbose_name_plural = "unregistered inventories"
        db_table = 'unregistered_inventories'
    def __str__(self):
        return self.name_unreg_aud
