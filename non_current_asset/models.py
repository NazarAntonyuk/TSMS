from django.db import models
from django.conf import settings

class NonCurrentAsset(models.Model):
    journal_code = models.CharField(max_length=20, verbose_name="Код кафедри")
    name_description = models.TextField(verbose_name="Найменування, стисла характеристика")
    acquisition_date = models.CharField(max_length=20, verbose_name="Дата придбання/введення в експлуатацію")
    inventory_number = models.CharField(max_length=50, verbose_name="Інвентарний номер")
    factory_number = models.CharField(max_length=50, verbose_name="Заводський номер", blank=True, null=True)
    passport_number = models.CharField(max_length=50, verbose_name="Паспортний номер", blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=20, verbose_name="Одиниця вимірювання")
    quantity_asset = models.IntegerField(verbose_name="Кількість")
    initial_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Первісна вартість", blank=True, null=True)
    arrival_mark = models.CharField(max_length=100, verbose_name="Відмітка про прибуття", blank=True, null=True)
    bux_quantity_asset = models.IntegerField(verbose_name="Кількість за бухгалтерськими даними", blank=True, null=True)
    bux_initial_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Первісна вартість за бухгалтерськими даними", blank=True, null=True)
    wear_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сума зносу", blank=True, null=True)
    balance_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Балансова вартість", blank=True, null=True)
    service_life = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Строк корисного використання", blank=True, null=True)
    other_details = models.TextField(verbose_name="Інші відомості", blank=True, null=True)
    placement = models.CharField(max_length=100, verbose_name="Розміщення", blank=True, null=True)
    decommissioning = models.CharField(max_length=50, verbose_name="Дата списання", blank=True, null=True)
    person_in_charge = models.CharField(max_length=100, verbose_name="Відповідальний", blank=True, null=True)


    def __str__(self):
        return self.name_description

    class Meta:
        db_table = 'non_current_asset'
        verbose_name = "Non Current Asset"
        verbose_name_plural = "Non Current Asset"