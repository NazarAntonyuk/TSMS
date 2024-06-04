from django.contrib import admin
from .models import JournalAppeals

@admin.register(JournalAppeals)
class JournalAppealsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JournalAppeals._meta.get_fields() if field.name != "id"]
    list_filter = [field.name for field in JournalAppeals._meta.get_fields() if field.name != "id"]
    search_fields = [field.name for field in JournalAppeals._meta.get_fields() if field.name != "id"]
