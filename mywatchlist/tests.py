from django.test import TestCase
from django.test import Client
# Create your tests here.

class Test(TestCase):
    def setUp (self):
        self.client = Client()
    def html_test(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    def html_test(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    def html_test(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)