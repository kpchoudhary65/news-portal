import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class NewsApiViewTests(APITestCase):
    valid_url = reverse('news')
    invalid_url = 'new'

    def test_valid_data_post(self):
        response = self.client.post(
            self.valid_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        message = response.json()['message']
        self.assertEqual(message, 'Record created')

    def test_invalid_data_post(self):
        response = self.client.post(
            self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_missing_data_post(self):
        response = self.client.post(format(json))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
