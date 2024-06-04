from django.db import models

class EquipmentType(models.Model):
    type_equipment = models.CharField(max_length=255, verbose_name="Тип обладнання")

    class Meta:
        verbose_name_plural = "Equipment Types"
        db_table = 'equipment_type'

    def __str__(self):
        return self.type_equipment

class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, verbose_name="Тип обладнання", blank=True, null=True)
    processor = models.CharField(max_length=255, verbose_name="Процесор", blank=True, null=True)
    ram_gb = models.CharField(max_length=255,verbose_name="ОЗУ (GB)", blank=True, null=True)
    ram_type = models.CharField(max_length=255, verbose_name="Тип ОЗУ", blank=True, null=True)
    hdd_volume = models.CharField(max_length=255,verbose_name="Об'єм HDD", blank=True, null=True)
    ssd_volume = models.CharField(max_length=255,verbose_name="Об'єм SSD", blank=True, null=True)
    motherboard = models.CharField(max_length=255, verbose_name="Материнська плата", blank=True, null=True)
    motherboard_socket = models.CharField(max_length=255, verbose_name="Сокет материнської плати", blank=True, null=True)
    power_supply = models.CharField(max_length=255, verbose_name="БЖ", blank=True, null=True)
    operating_system = models.CharField(max_length=255, verbose_name="Операційна система", blank=True, null=True)
    office_software = models.CharField(max_length=255, verbose_name="Офісне ПЗ", blank=True, null=True)
    specialized_software = models.CharField(max_length=255, verbose_name="Спеціалізоване ПЗ", blank=True, null=True)
    screen_name = models.CharField(max_length=255, verbose_name="Назва монітору", blank=True, null=True)
    screen_diagonal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Діагональ екрану", blank=True, null=True)
    screen_resolution = models.CharField(max_length=255, verbose_name="Роздільна здатність екрану", blank=True, null=True)
    projector_name = models.CharField(max_length=255, verbose_name="Назва проектору", blank=True, null=True)
    projector_type = models.CharField(max_length=255, verbose_name="Тип проектора", blank=True, null=True)
    projector_resolution = models.CharField(max_length=255, verbose_name="Роздільна здатність проектора", blank=True, null=True)
    router_name = models.CharField(max_length=255, verbose_name="Назва комутатора", blank=True, null=True)
    router_speed = models.CharField(max_length=255,verbose_name="Швидкість комутатора", blank=True, null=True)
    ports_number = models.CharField(max_length=255, verbose_name="Кількість портів/занятих портів", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Equipment"
        db_table = 'equipment'

    def __str__(self):
        fields_with_values = []

        # Додаємо тип обладнання як перше значення
        if self.equipment_type:
            fields_with_values.append(f"{self.equipment_type.type_equipment}")

        # Проходимося по всіх полях моделі
        for field in self._meta.get_fields():
            # Перевіряємо, що поле не є зв'язком та не містить None
            if not field.is_relation and getattr(self, field.name, None):
                field_label = field.verbose_name
                field_value = getattr(self, field.name)
                fields_with_values.append(f"{field_label}: {field_value}")

        # Вертаємо рядок, де всі непорожні поля з'єднані через пробіл
        return '  '.join(fields_with_values)