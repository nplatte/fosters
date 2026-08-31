from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestCats(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        return super().setUp()

    def test_can_add_cat(self):
        pass

    def test_can_view_cat(self):
        pass

    def test_can_delete_cat(self):
        pass

    def test_can_update_cat(self):
        pass

    def test_can_add_event_to_cat(self):
        pass