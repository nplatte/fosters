

class BaseTestCaseMixin:

    fixtures = ['cats', 'events']
    tc_name = None

    def setUp(self):
        self.tc = self.get_test_case()

    def test_GET_returns_200(self):
        response = self.client.get(self.tc.url)
        self.assertEqual(response.status_code, 200)

class RedirectTestCaseMixin(BaseTestCaseMixin):

    def test_POST_success_redirect_to_page(self):
        response = self.client.post(self.tc.url, self.tc.valid_data)
        self.assertRedirects(response, self.tc.redirect_url)


class CreateViewTestCaseMixin(RedirectTestCaseMixin):

    def test_POST_makes_model(self):
        old_count = self.tc.model.objects.count()
        response = self.client.post(self.tc.url, self.tc.valid_data)
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
        self.client.post(self.tc.url, data=self.tc.valid_data)
        new_count = self.tc.model.objects.count()
        self.assertLess(new_count, old_count)
