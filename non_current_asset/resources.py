from import_export import resources
from .models import NonCurrentAsset

class NonCurrentAssetResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        """
        Цей метод викликається перед імпортом кожного рядка,
        щоб переконатися, що записи завжди створюються як нові,
        ігноруючи існуючі записи в базі даних.
        """
        row['id'] = None  # Видаляємо ID, щоб Django не намагався знайти і оновити існуючий запис

    class Meta:
        model = NonCurrentAsset
        import_id_fields = ()  # Видаляємо поля ідентифікації
        exclude = ('id',)  # Ігноруємо поле ID при імпорті
        fields = [
            'journal_code', 'name_description',
            'acquisition_date', 'inventory_number', 'factory_number', 'passport_number',
            'unit_of_measurement', 'quantity_asset',
            'initial_cost', 'arrival_mark', 'bux_quantity_asset', 'bux_initial_cost', 'wear_amount',
            'balance_value', 'service_life', 'other_details',
            'placement', 'decommissioning', 'person_in_charge',
        ]
