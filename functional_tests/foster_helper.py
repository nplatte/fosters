from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class TestHelper(StaticLiveServerTestCase):

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
