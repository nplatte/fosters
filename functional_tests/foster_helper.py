from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

    def count_elements_by_class(self, class_name):
        return len(self.browser.find_elements(By.CLASS_NAME, class_name))

    def fill_in_form_by_ids(self, data_by_id):
        for id, data in data_by_id.items():
            if id == "cat":
                self._fill_in_select_widget(id, data)
            else:
                input_element = self.findElementByID(f"id_{id}")
                try:
                    input_element.clear()
                except:
                    pass
                input_element.send_keys(data)
        submit_btn = self.findElementByID("submit_btn")
        submit_btn.click()

    def _fill_in_select_widget(self, id, data):
        element = Select(self.findElementByID(f"id_{id}"))
        element.select_by_value(data)

    def assertPageHasID(self, id_name):
        count = len(self.browser.find_elements(By.ID, id_name))
        self.assertEqual(count, 1, f"missing ID {id_name}")

    def assertTitleEquals(self, title):
        self.assertEqual(self.browser.title, title)

    def log_in_to_site(self):
        self.browser.get(f'{self.live_server_url}{reverse('landing')}')
        self.assertTitleEquals("Home Page")

    def navigate_to_cats_page(self):
        self.find_and_click("cats_link")
        self.assertTitleEquals("Cats")

    def navigate_to_litters_page(self):
        self.find_and_click("litters_link")
        self.assertTitleEquals("Litters")

    def find_and_click(self, id):
        element = self.findElementByID(id)
        element.click()

