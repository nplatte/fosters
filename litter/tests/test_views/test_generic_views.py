from django.test import TestCase
from dataclasses import dataclass
from django.db import models
from django.urls import reverse
from litter.models import Cat


@dataclass
class AddViewTestCase:
    name: str
    url: str
    model: type[models.Model]
    valid_data: dict
    redirect_url: str

class TestAddViews(TestCase):

    fixtures = ['cats']

    def setUp(self):
        cat_test_case = AddViewTestCase(
            name="Add Cat Test",
            url = reverse('add_cat'),
            model=Cat,
            valid_data={"name": "Cat",
                "estimated_date_of_birth": "01/01/1992",
                "gender": "male", "color": "black",},
            redirect_url=reverse("cat", kwargs={"pk": Cat.objects.count()+1}))
        
        self.test_cases = [ cat_test_case, ]
        return super().setUp()
    
    def test_GET_returns_200(self):
        for tc in self.test_cases:
            with self.subTest(name=tc.name):
                response = self.client.get(tc.url)
                self.assertEqual(response.status_code, 200)

    def test_POST_makes_cat(self):
        for tc in self.test_cases:
            with self.subTest(name=tc.name):
                old_count = tc.model.objects.count()
                self.client.post(tc.url, tc.valid_data)
                new_count = tc.model.objects.count()
                self.assertGreater(new_count, old_count)

    def test_POST_success_sends_to_cat_page(self):
        for tc in self.test_cases:
            with self.subTest(name=tc.name):
                response = self.client.post(tc.url, tc.valid_data)
                self.assertRedirects(response, tc.redirect_url)
