from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestLitter(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        cls.browser = webdriver.Firefox(options=options)        

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        return super().tearDownClass()

    def setUp(self):
        self.browser.delete_all_cookies()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

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