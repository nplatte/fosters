from django.test import TestCase
from django.urls import reverse
from litter.models import Litter


class TestViewLitter(TestCase):

    fixture = ['litters']

    def setUp(self):
        self.url = reverse('litter', kwargs={"pk": 1})
        return super().setUp()

    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class TestAddLitter(TestCase):

    def setUp(self):
        self.url = reverse('add_litter')
        self.data = {"name": "Test Litter"}
        return super().setUp()

    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_POST_makes_new_litter(self):
        old_count = Litter.objects.count()
        self.client.post(self.url, self.data)
        new_count = Litter.objects.count()
        self.assertGreater(new_count, old_count)

    def test_POST_redirects_to_cats_page(self):
        response = self.client.post(self.url, self.data)
        self.assertRedirects(response, reverse("litter", kwargs={"pk": 1}))
