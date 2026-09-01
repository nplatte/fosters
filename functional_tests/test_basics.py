from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from litter.models import Cat


class TestCats(StaticLiveServerTestCase):

    fixtures = [ "cats" ]

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
        # the user logs in
        self.browser.get(f'{self.live_server_url}{reverse('landing')}')
        self.assertEqual(self.browser.title, "Home Page")
        # they click the cats button
        cats_link = self.browser.find_element(By.ID, "cats_link")
        cats_link.click()
        # they click the cat they want to see
        cat_link = self.browser.find_element(By.ID, "cat_1_link")
        cat_link.click()
        test_cat = Cat.objects.get(pk=1)
        self.assertEqual(self.browser.title, test_cat.name)
        # they see the cats information
        cat_ids = [
            ("cat_name", test_cat.name), ("cat_dob", test_cat.estimated_date_of_birth.strftime("%Y-%m-%d")), 
            ("cat_microchip", f"{test_cat.microchip} inserted on {test_cat.microchip_inserted_on.strftime("%Y-%m-%d")}"),
            ("cat_internal", test_cat.internal_id), ("cat_gender", test_cat.gender), ("cat_color", test_cat.color),
            ("cat_litter", str(test_cat.litter))
        ]
        for id in cat_ids:
            element = self.browser.find_element(By.ID, id[0])
            self.assertEqual(element.text, id[1], msg=f"{id[0]}")
        # they log out

    def test_can_delete_cat(self):
        self.fail("finish the test")

    def test_can_update_cat(self):
        edit_cat = Cat.objects.get(pk=1)
        # the user logs into the site
        self.browser.get(f'{self.live_server_url}{reverse('landing')}')
        self.assertEqual(self.browser.title, "Home Page")
        # they click the cats page
        cats_link = self.browser.find_element(By.ID, "cats_link")
        cats_link.click()
        self.assertEqual(self.browser.title, "Cats")
        old_count = self.browser.find_elements(By.CLASS_NAME, "cat")
        # they click the edit cat link
        cats_link = self.browser.find_element(By.ID, "edit_1_link")
        cats_link.click()
        self.assertEqual(self.browser.title, f"Edit {edit_cat.name}")
        # they see the current information
        cat_ids = [
            ("cat_name", edit_cat.name), ("cat_dob", edit_cat.estimated_date_of_birth.strftime("%Y-%m-%d")), 
            ("cat_microchip", f"{edit_cat.microchip} inserted on {edit_cat.microchip_inserted_on.strftime("%Y-%m-%d")}"),
            ("cat_internal", edit_cat.internal_id), ("cat_gender", edit_cat.gender), ("cat_color", edit_cat.color),
            ("cat_litter", str(edit_cat.litter))
        ]
        for id in cat_ids:
            input = self.browser.find_element(By.ID, f"{id[0]}_input")
            self.assertEqual(input.value, id[1])
        # they make a change to the name
        name_input = self.browser.find_element(By.ID, "cat_name_input")
        name_input.clear()
        name_input.send_keys("Hello Kitty")
        # they save
        submit = self.browser.find_element(By.ID, "submit_btn")
        submit.click()
        # they get redirected to the cats page
        edited_cat = Cat.objects.get(pk=1)
        self.assertEqual(self.browser.title, "Hello Kitty")
        # they click the all cats link
        cats_link = self.browser.find_element(By.ID, "cats_link")
        cats_link.click()
        self.assertEqual(self.browser.title, "Cats")
        # they see the same number of cats
        new_count = self.browser.find_elements(By.CLASS_NAME, "cat")
        self.assertEqual(new_count, old_count)

    def test_can_add_event_to_cat(self):
        self.fail("finish the test")