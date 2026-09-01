from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from time import sleep


class TestCats(StaticLiveServerTestCase):

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
        self.valid_data = {
            "name": "Wiggles", "estimated_date_of_birth": "01/01/1992",
            "gender": "male", "color": "black",
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_can_add_cat(self):
        # the user logs into the website
        self.browser.get(f'{self.live_server_url}{reverse('landing')}')
        # the user is on the home page
        self.assertEqual(self.browser.title, "Home Page")
        # they click the view cats page
        cats_link = self.browser.find_element(By.ID, "cats_link")
        cats_link.click()
        # they see some cats
        self.assertEqual(self.browser.title, "Cats")
        old_count = len(self.browser.find_elements(By.CLASS_NAME, "cat"))
        # they click the add cat button
        create_cat_link = self.browser.find_element(By.ID, "create_cat_link")
        create_cat_link.click()
        # they are taken to the add cat page
        self.assertEqual(self.browser.title, "Add Cat")
        # they enter in the cat inforamtion
        for field_name, data in self.valid_data.items():
            input = self.browser.find_element(By.ID, f'id_{field_name}')
            input.send_keys(data)
        # they click enter and are taken to the cat's page
        submit_btn = self.browser.find_element(By.ID, "submit_btn")
        submit_btn.click()
        self.assertEqual(self.browser.title, f"{self.valid_data['name']}")
        # they click cats and see the new cat added
        cats_link = self.browser.find_element(By.ID, "cats_link")
        cats_link.click()
        new_count = len(self.browser.find_elements(By.CLASS_NAME, "cat"))
        self.assertGreater(new_count, old_count)

    def test_can_view_cat(self):
        self.fail("finish the test")

    def test_can_delete_cat(self):
        self.fail("finish the test")

    def test_can_update_cat(self):
        self.fail("finish the test")

    def test_can_add_event_to_cat(self):
        self.fail("finish the test")