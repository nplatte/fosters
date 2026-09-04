from dataclasses import dataclass, field
from django.db import models

@dataclass
class ViewTestCase:
    name: str = ""
    url: str = ""
    model: type[models.Model] = None
    valid_data: dict = field(default_factory=dict)
    redirect_url: str = ""
    fields: list[str] = field(default_factory=list)


class BaseTestCaseMixin:

    fixtures = ['cats', 'events']
    tc_name = None

    def setUp(self):
        self.tc = self.get_test_case()
        return super().setUp()

    def test_GET_returns_200(self):
        response = self.client.get(self.tc.url)
        self.assertEqual(response.status_code, 200)

class RedirectTestCaseMixin(BaseTestCaseMixin):

    def test_POST_success_redirect_to_page(self):
        response = self.client.post(self.tc.url, self.tc.valid_data)
        if response.status_code == 200:
            form = response.context['form']
            self.assertTrue(
                form.is_valid(),
                msg=f"Form was invalid: {form.errors.as_data()}"
            )
        self.assertRedirects(response, self.tc.redirect_url)

    def test_ids_on_page(self):
        response = self.client.get(self.tc.url)
        html = response.content.decode()
        for field_name in self.tc.fields:
            self.assertIn(f"id_{field_name}", html)


class CreateViewTestCaseMixin(RedirectTestCaseMixin):

    def test_POST_makes_model(self):
        old_count = self.tc.model.objects.count()
        self.client.post(self.tc.url, self.tc.valid_data)
        new_count = self.tc.model.objects.count()
        self.assertGreater(new_count, old_count)


class UpdateViewTestCaseMixin(RedirectTestCaseMixin):

    def test_POST_edits_model(self):
        old_count = self.tc.model.objects.count()
        self.client.post(self.tc.url, self.tc.valid_data)
        new_count = self.tc.model.objects.count()
        self.assertEqual(new_count, old_count)


class DeleteViewTestCaseMixin(RedirectTestCaseMixin):

    def test_POST_deletes_model(self):
        old_count = self.tc.model.objects.count()
        self.client.post(self.tc.url, self.tc.valid_data)
        new_count = self.tc.model.objects.count()
        self.assertLess(new_count, old_count)
