from django.conf import settings
from django.db import models
from equipment.models import Equipment
from non_current_asset.models import NonCurrentAsset


class Auditorium(models.Model):
    number = models.CharField(max_length=255, verbose_name="Номер аудиторії", blank=True, null=True)
    description_aud = models.TextField(verbose_name="Опис", blank=True, null=True)
    head = models.CharField(max_length=255, verbose_name="ПІБ завідувача", blank=True, null=True)

    class Meta:
        verbose_name = "Auditorium"
        verbose_name_plural = "Auditoriums"
        db_table = 'auditorium'

    def __str__(self):
        return f"Auditorium {self.number} - {self.description_aud}"

class EquipmentInAuditorium(models.Model):
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE, verbose_name="Номер аудиторії")
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, verbose_name="Обладнання", blank=True, null=True)
    non_current_asset = models.ForeignKey(NonCurrentAsset, on_delete=models.SET_NULL, verbose_name="Необоротний актив", blank=True, null=True)
    last_service_date = models.DateField(verbose_name="Дата останнього обслуговування", blank=True, null=True)
    repair_date = models.DateField(verbose_name="Дата ремонту", blank=True, null=True)
    note_equip = models.TextField(verbose_name="Примітка", blank=True, null=True)


    class Meta:
        verbose_name = "Equipment in Auditorium"
        verbose_name_plural = "Equipment in Auditoriums"
        db_table = 'equipment_in_auditorium'

    def __str__(self):
        return f"{self.auditorium} - {self.equipment}"
