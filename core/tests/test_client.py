from core.views import landing_page
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/accounts/')
        self.assertEqual(response.status_code, 200)
