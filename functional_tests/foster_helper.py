from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.urls import reverse


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

    def findElementByID(self, id_name):
        self.assertPageHasID(id_name)
        return self.browser.find_element(By.ID, id_name)

    def assertPageHasID(self, id_name):
        count = len(self.browser.find_elements(By.ID, id_name))
        self.assertEqual(count, 1)

    def assertTitleEquals(self, title):
        self.assertEqual(self.browser.title, title)

    def log_in_to_site(self):
        self.browser.get(f'{self.live_server_url}{reverse('landing')}')
        self.assertTitleEquals("Home Page")

    def navigate_to_cats_page(self):
        cats_link = self.findElementByID('cats_link')
        cats_link.click()
        self.assertTitleEquals("Cats")

