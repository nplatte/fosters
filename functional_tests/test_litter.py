from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestLitter(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        return super().setUp()

    def test_can_add_litter(self):
        pass

    def test_can_add_cat_to_litter(self):
        pass

    def test_can_update_litter_info(self):
        pass

    def test_can_remove_cats_in_litter(self):
        pass

    def test_can_add_events_to_cats_in_litter(self):
        pass