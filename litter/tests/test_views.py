from django.test import TestCase
from django.urls import reverse


class TestBasicGET(TestCase):

    def setUp(self):
        self.url_names = [
            "landing", "add_cat", "edit_cat"
        ]
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_returns_200(self):
        for url_name in self.url_names:
            with self.subTest(url=url_name):
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)