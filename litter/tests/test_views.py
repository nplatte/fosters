from django.test import TestCase
from django.urls import reverse


class TestBasicGET(TestCase):

    fixtures = ['cats']

    def setUp(self):
        self.url_names = [
            ["landing", {}], ["add_cat", {}], ["edit_cat", {"pk": 1}],
            ['all_cats', {}], ['cat', {"pk":1}]
        ]
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_returns_200(self):
        for url_name in self.url_names:
            with self.subTest(url=url_name[0]):
                url = reverse(url_name[0], kwargs=url_name[1])
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)