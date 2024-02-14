from django.test import TestCase
from restaurant.models import MenuItem

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream", price=80, Inventory=100)
        self.assertEqual(item.Title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.Inventory, 100)