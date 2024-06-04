from django.contrib import admin
from .models import Equipment, EquipmentType

@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ['type_equipment']
    search_fields = ['type_equipment']

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_filter = (
        'equipment_type__type_equipment',
        'processor',
        'ram_gb',
        'ram_type',
        'hdd_volume',
        'ssd_volume',
        'motherboard',
        'motherboard_socket',
        'power_supply',
        'operating_system',
        'office_software',
        'specialized_software',
        'screen_diagonal',
        'screen_resolution',
        'projector_type',
        'projector_resolution',
        'router_speed',
        'ports_number',
    )

    search_fields = (
        'equipment_type__type_equipment',
        'processor',
        'ram_gb',
        'ram_type',
        'hdd_volume',
        'ssd_volume',
        'motherboard',
        'motherboard_socket',
        'power_supply',
        'operating_system',
        'office_software',
        'specialized_software',
        'screen_name',
        'screen_diagonal',
        'screen_resolution',
        'projector_type',
        'projector_resolution',
        'router_speed',
        'ports_number',
        'projector_name',
        'router_name',
    )

    # Організація полів у секціях форми адміністратора
    fieldsets = (
        (None, {
            'fields': ('equipment_type',)
        }),
        ('Для ПК', {
            'fields': (
                'processor',
                'ram_gb',
                'ram_type',
                'hdd_volume',
                'ssd_volume',
                'motherboard',
                'motherboard_socket',
                'power_supply',
            )
        }),
        ('Програмне забезпечення та ОС', {
            'fields': (
                'operating_system',
                'office_software',
                'specialized_software',
            )
        }),
        ('Для моніторів', {
            'fields': (
                'screen_name',
                'screen_diagonal',
                'screen_resolution',
            )
        }),
        ('Для проекторів', {
            'fields': (
                'projector_name',
                'projector_type',
                'projector_resolution',
            )
        }),
        ('Для мережевого обладнання', {
            'fields': (
                'router_name',
                'router_speed',
                'ports_number',
            )
        }),
    )
