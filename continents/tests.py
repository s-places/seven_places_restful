"""Tests using DRF classes"""
from continents.models import Continent
from rest_framework.test import APITestCase
from rest_framework import status


class TestAPI(APITestCase):
    """Testing of API"""
    def setUpTestData(self):
        """Data initializing"""
        continent_data = {
            "id": 1,
            "name": "Asia",
            "place": "Tokyo",
            "population": 13_960_236,
            "overview": "Capital of Japan",
            "languages": "Japanese",
            "first_image": None,
            "second_image": None,
            "third_image": None,
        }

        Continent.objects.create(**continent_data)

    def test_model(self):
        """Data creating"""
        self.assertEqual(Continent.objects.count(),1)

    def test_api(self):
        """Responses"""
        response_single = self.client.get('/continent/1')
        response_list = self.client.get('/continents/')
        response_bad = self.client.get('/continent/333')
        self.assertEquals(response_single.status_code,status.HTTP_200_OK)
        self.assertEquals(response_list.status_code,status.HTTP_200_OK)
        self.assertEquals(response_bad.status_code,status.HTTP_404_NOT_FOUND)