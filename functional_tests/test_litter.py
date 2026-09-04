from functional_tests.foster_helper import TestHelper
from litter.models import Litter


class TestLitter(TestHelper):

    fixtures = ['litters']

    def setUp(self):
        self.browser.delete_all_cookies()
        return super().setUp()

    def test_can_add_litter(self):
        # the user logs into the website
        self.log_in_to_site()
        # they go to the litters page
        self.navigate_to_litters_page()
        old_count = self.count_elements_by_class("litter")
        # they click add litter
        self.find_and_click('add_link')
        self.assertTitleEquals("Add Litter")
        # they fill out the form
        data = {
            "name": "new Litter"
        }
        self.fill_in_form_by_ids(data)
        # they are redirected to the litters page
        self.assertTitleEquals("Litters")
        # they see a new litter created
        new_count = self.count_elements_by_class("litter")
        self.assertGreater(new_count, old_count)

    def test_user_can_delete_litter(self):
        test_litter = Litter.objects.get(pk=1)
        # the user logs into the website
        self.log_in_to_site()
        # they go to the litter page
        self.navigate_to_litters_page()
        # they see the litter they want to delete
        old_count = self.count_elements_by_class("litter")
        self.assertGreater(old_count, 0)
        # they click the link
        self.find_and_click(f"delete_{test_litter.pk}_link")
        self.assertTitleEquals(f'Delete {test_litter.name}')
        # they click confirm
        self.find_and_click("confirm_delete_btn")
        # they are taken to the litter page
        self.assertTitleEquals("Litters")
        new_count = self.count_elements_by_class("litter")
        self.assertLess(new_count, old_count)

    def test_can_update_litter(self):
        test_litter = Litter.objects.get(pk=1)
        # the user logs into the site
        self.log_in_to_site()
        # the user goes to the litters page
        self.navigate_to_litters_page()
        # they click on the update litter link by the litter they want to change
        self.find_and_click("update_1_link")
        self.assertTitleEquals(f'Edit {test_litter.name}')
        # they enter the new name
        self.fill_in_form_by_ids({"name": "Socks"})
        # they are taken to the litter's page
        test_litter = Litter.objects.get(pk=1)
        self.assertTitleEquals(test_litter.name)
        # they see the update
        litter_name = self.findElementByID("litter_name")
        self.assertEqual(litter_name.text, test_litter.name)

    def test_user_can_view_litter(self):
        test_litter = Litter.objects.get(pk=1)
        # the user logs into the site
        self.log_in_to_site()
        # they go to the litters page
        self.navigate_to_litters_page()
        # they see the existing litter name
        litter_name = self.findElementByID("litter_1_name")
        self.assertEqual(litter_name.text, test_litter.name)
        # they click the view litter link
        self.find_and_click("view_1_link")
        self.assertTitleEquals(test_litter.name)
        # they see the name
        litter_name = self.findElementByID("litter_name")
        self.assertEqual(litter_name.text, test_litter.name)

    def test_can_add_cat_to_litter(self):
        self.fail("finish the test")

    def test_can_remove_cats_in_litter(self):
        self.fail("finish the test")

    def test_can_add_events_to_cats_in_litter(self):
        self.fail("finish the test")