from django.test import TestCase
from django.urls import reverse


class TestLitterGET(TestCase):

    def setUp(self):
        self.url = reverse("landing")
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_dashboard_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)