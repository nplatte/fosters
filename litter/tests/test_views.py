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


class TestAddCat(TestCase):

    def setUp(self):
        self.url = reverse('add_cat')
        self.data = {
            "name": "Cat",
            "estimated_date_of_birth": "01/01/1992",
            "gender": "male", "color": "black",
        }
        return super().setUp()

    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_POST_makes_cat(self):
        old_count = Cat.objects.count()
        self.client.post(self.url, self.data)
        new_count = Cat.objects.count()
        self.assertGreater(new_count, old_count)

    def test_POST_success_sends_to_cat_page(self):
        response = self.client.post(self.url, self.data)
        new_cat = Cat.objects.all().last()
        self.assertRedirects(response, reverse("cat", kwargs={"pk": new_cat.pk}))


class TestEditCat(TestCase):

    fixtures = ['cats']

    def setUp(self):
        self.url = reverse('edit_cat', kwargs={"pk": 1})
        self.data = {
            "name": "Cat", 'microchip': "1562",
            "estimated_date_of_birth": "01/01/1992",
            "gender": "male", "color": "green",
        }
        return super().setUp()

    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_POST_edits_cat(self):
        old_count = Cat.objects.count()
        self.client.post(self.url, self.data)
        new_count = Cat.objects.count()
        self.assertEqual(new_count, old_count)

    def test_POST_success_sends_to_cat_page(self):
        response = self.client.post(self.url, self.data)
        self.assertRedirects(response, reverse("cat", kwargs={"pk": 1}))
