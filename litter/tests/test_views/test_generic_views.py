from django.test import TestCase
from litter.tests.test_views.build_test_cases import build_add_view_test_cases


class TestAddViews(TestCase):

    fixtures = ['cats']

    def setUp(self):
        self.test_cases = build_add_view_test_cases()
        return super().setUp()
    
    def test_GET_returns_200(self):
        for tc in self.test_cases:
            with self.subTest(name=f"{tc.name}: Status 200"):
                response = self.client.get(tc.url)
                self.assertEqual(response.status_code, 200)

    def test_POST_makes_model(self):
        for tc in self.test_cases:
            with self.subTest(name=f"{tc.name}: POST makes model"):
                old_count = tc.model.objects.count()
                self.client.post(tc.url, tc.valid_data)
                new_count = tc.model.objects.count()
                self.assertGreater(new_count, old_count)

    def test_POST_success_sends_to_cat_page(self):
        for tc in self.test_cases:
            with self.subTest(name=f"{tc.name}: POST redirects to expected url"):
                response = self.client.post(tc.url, tc.valid_data)
                self.assertRedirects(response, tc.redirect_url)
