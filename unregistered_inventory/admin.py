from django.contrib import admin
from .models import UnregisteredInventory

@admin.register(UnregisteredInventory)
class UnregisteredInventoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UnregisteredInventory._meta.get_fields() if field.name != "id"]
    list_filter = [field.name for field in UnregisteredInventory._meta.get_fields() if field.name != "id"]
    search_fields = [field.name for field in UnregisteredInventory._meta.get_fields() if field.name != "id"]
