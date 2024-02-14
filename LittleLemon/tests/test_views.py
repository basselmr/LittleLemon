from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = MenuItem.objects.create(Title="Menu 1", price=10.99, Inventory=5)
        self.menu2 = MenuItem.objects.create(Title="Menu 2", price=15.99, Inventory=5)

    def test_getall(self):
        url = reverse('menu-view')
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = MenuSerializer([self.menu1, self.menu2], many=True).data
        self.assertEqual(response.data, serialized_data)