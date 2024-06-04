from django.db import models
from django.conf import settings

class JournalAppeals(models.Model):
    problem_aud = models.CharField(verbose_name="№ аудиторії",max_length=255, blank=True, null=True)
    description_problem = models.TextField(verbose_name="Опис проблеми",blank=True, null=True)
    contact_name = models.CharField(verbose_name="Ім'я",max_length=255, blank=True, null=True)
    tel_number = models.CharField(verbose_name="Телефон",max_length=255, blank=True, null=True)
    date_appeals = models.DateField(verbose_name="Дата подання заявки",blank=True, null=True)
    Status = models.CharField(verbose_name="Статус виконання", max_length=255, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Journal of appeals"
        db_table = 'Journal of appeals'
    def __str__(self):
        return f"{self.Status} - {self.problem_aud}"
