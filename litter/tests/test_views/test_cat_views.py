from django.test import TestCase
from django.urls import reverse
from litter.models import Cat


class TestBasicGET(TestCase):

    fixtures = ['cats']

    def setUp(self):
        self.url_names = [
            ["landing", {}],
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


class TestDeleteCat(TestCase):

    fixtures = ['cats']

    def setUp(self):
        self.url = reverse('delete_cat', kwargs={"pk": 1})
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_POST_deletes_cat(self):
        old_count = Cat.objects.count()
        self.client.post(self.url, data={})
        new_count = Cat.objects.count()
        self.assertLess(new_count, old_count)
