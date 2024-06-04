from django.test import TestCase
from .models import NonCurrentAsset

class NonCurrentAssetTestCase(TestCase):
    def setUp(self):
        # Створення інстанса моделі NonCurrentAsset
        NonCurrentAsset.objects.create(
            journal_code="001",
            name_description="Лазерний принтер",
            acquisition_date="2021-01-01",
            inventory_number="INV12345",
            unit_of_measurement="шт",
            quantity_asset=1,
            initial_cost=5000.00
        )

    def test_non_current_asset_creation(self):
        """Перевіряє, чи коректно створюється об'єкт NonCurrentAsset."""
        asset = NonCurrentAsset.objects.get(journal_code="001")
        self.assertEqual(asset.name_description, "Лазерний принтер")
        self.assertEqual(asset.inventory_number, "INV12345")
        self.assertEqual(asset.initial_cost, 5000.00)

    def test_non_current_asset_string_representation(self):
        """Тестує правильність роботи методу __str__."""
        asset = NonCurrentAsset.objects.get(journal_code="001")
        self.assertEqual(str(asset), "Лазерний принтер")
