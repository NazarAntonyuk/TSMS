from django.apps import AppConfig


class UnregisteredInventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unregistered_inventory'
