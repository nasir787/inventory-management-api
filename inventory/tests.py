from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Item

# Create a user for testing JWT authentication:
class ItemAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Obtain JWT token
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        # Set up a sample item for testing
        self.item = Item.objects.create(
            name='Test Item',
            description='Test Description',
            quantity=5,  # Add quantity here
            price='49.99'  # Add price here
        )

# Test the POST endpoint for creating an item:
    def test_create_item(self):
        data = {
            'name': 'New Item',
            'description': 'New Item Description',
            'quantity': 10,  # Add quantity
            'price': '99.99'  # Add price (as a string, if you are using DecimalField)
        }
        response = self.client.post(reverse('item-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)

# Test the GET endpoint for retrieving an item:
    def test_get_item(self):
        response = self.client.get(reverse('item-detail', args=[self.item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

# Test the PUT endpoint for updating an item:
    def test_update_item(self):
        data = {
            'name': 'Updated Item',
            'description': 'Updated Description',
            'quantity': 15,
            'price': '79.99'
        }
        # Use the 'item-update' endpoint instead of 'item-detail'
        response = self.client.put(reverse('item-update', args=[self.item.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')
        self.assertEqual(self.item.quantity, 15)
        self.assertEqual(str(self.item.price), '79.99')


# Test the DELETE endpoint for deleting an item:
    def test_delete_item(self):
        # Use the 'item-delete' endpoint, matching the URL pattern
        response = self.client.delete(reverse('item-delete', args=[self.item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

