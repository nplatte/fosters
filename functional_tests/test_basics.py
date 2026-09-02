from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from litter.models import Cat
from functional_tests.foster_helper import TestHelper


class TestCats(TestHelper):

    fixtures = [ "cats" ]

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
        self.log_in_to_site()
        # they click the view cats page
        self.navigate_to_cats_page()
        old_count = self.count_elements_by_class("cat")
        # they click the add cat button
        create_cat_link = self.browser.find_element(By.ID, "create_cat_link")
        create_cat_link.click()
        # they are taken to the add cat page
        self.assertEqual(self.browser.title, "Add Cat")
        # they enter in the cat inforamtion
        self.fill_in_form_by_ids(self.valid_data)
        # they are back at the Cat's page
        self.assertEqual(self.browser.title, f"{self.valid_data['name']}")
        # they click cats and see the new cat added
        self.navigate_to_cats_page()
        new_count = self.count_elements_by_class("cat")
        self.assertGreater(new_count, old_count)

    def test_can_view_cat(self):
        # the user logs in
        self.log_in_to_site()
        # they click the cats button
        cats_link = self.browser.find_element(By.ID, "cats_link")
        cats_link.click()
        # they click the cat they want to see
        test_cat = Cat.objects.get(pk=1)
        self.find_and_click(f"view_{test_cat.pk}_link")
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
        # the user logs into the server
        self.log_in_to_site()
        # they click the view cats page
        self.navigate_to_cats_page()
        # they see a cat
        old_count = len(self.browser.find_elements(By.CLASS_NAME, "cat"))
        self.assertGreater(old_count, 0)
        # they want to delete the cat
        test_cat = Cat.objects.get(pk=1)
        delete_link = self.browser.find_element(By.ID, f"delete_{test_cat.pk}_link")
        # they click the delete link
        delete_link.click()
        self.assertEqual(self.browser.title, f"Delete {test_cat.name}")
        # then click confirm
        confirm = self.browser.find_element(By.ID, "confirm_delete_btn")
        confirm.click()
        # they are returned to the cats page
        self.assertEqual(self.browser.title, "Cats")
        # they see one less cat
        new_count = len(self.browser.find_elements(By.CLASS_NAME, "cat"))
        self.assertLess(new_count, old_count)

    def test_can_update_cat(self):
        edit_cat = Cat.objects.get(pk=1)
        # the user logs into the site
        self.log_in_to_site()
        # they click the cats page
        self.navigate_to_cats_page()
        old_count = self.count_elements_by_class("cat")
        # they click the edit cat link
        cats_link = self.browser.find_element(By.ID, "edit_1_link")
        cats_link.click()
        self.assertEqual(self.browser.title, f"Edit {edit_cat.name}")
        # they see the current information
        cat_ids = [
            ("name", edit_cat.name), ("estimated_date_of_birth", edit_cat.estimated_date_of_birth.strftime("%Y-%m-%d")), 
            ("microchip", edit_cat.microchip), ("microchip_inserted_on", edit_cat.microchip_inserted_on.strftime("%Y-%m-%d")),
            ("internal_id", edit_cat.internal_id), ("gender", edit_cat.gender), ("color", edit_cat.color),
        ]
        for id in cat_ids:
            input = self.browser.find_element(By.ID, f"id_{id[0]}")
            self.assertEqual(input.get_attribute("value"), id[1])
        # they make a change to the name
        name_input = self.browser.find_element(By.ID, "id_name")
        name_input.clear()
        name_input.send_keys("Hello Kitty")
        # they save
        submit = self.browser.find_element(By.ID, "submit_btn")
        submit.click()
        # they get redirected to the cats page
        edited_cat = Cat.objects.get(pk=1)
        self.assertEqual(self.browser.title, "Hello Kitty")
        # they click the all cats link
        self.navigate_to_cats_page()
        # they see the same number of cats
        new_count = self.count_elements_by_class("cat")
        self.assertEqual(new_count, old_count)


class TestEvent(TestHelper):

    fixtures = [ "cats" ]

    def setUp(self):
        self.browser.delete_all_cookies()
        self.valid_data = {
            "weight": "123", "medications": "Clav, Vycodin",
            "condition": "is super cute", "cat": f"{Cat.objects.get(pk=1).pk}",
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_add_event(self):
        # the user logs into the site
        self.log_in_to_site()
        # they want to add an event to a cat
        # they go to the cat page
        self.navigate_to_cats_page()
        test_cat = Cat.objects.get(pk=1)
        self.find_and_click(f"view_{test_cat.pk}_link")
        self.assertEqual(self.browser.title, test_cat.name)
        old_count = self.count_elements_by_class("event")
        # they click add event
        self.find_and_click("add_event")
        self.assertEqual(self.browser.title, "Add Event")
        # they enter the event info and hit submit
        self.fill_in_form_by_ids(self.valid_data)
        # they are taken to the cat page
        self.assertEqual(self.browser.title, test_cat.name)
        # they see the new event
        new_count = self.count_elements_by_class("event")
        self.assertGreater(new_count, old_count)
        # they log off


    def test_view_event(self):
        pass
