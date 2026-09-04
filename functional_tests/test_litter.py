from functional_tests.foster_helper import TestHelper


class TestLitter(TestHelper):

    def setUp(self):
        self.browser.delete_all_cookies()
        return super().setUp()

    def test_can_add_litter(self):
        # the user logs into the website
        self.log_in_to_site()
        # they go to the litters page
        self.find_and_click('litters_link')
        self.assertTitleEquals("Litters")
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
        self.fail("finish the test")

    def test_can_update_litter(self):
        self.fail("finish the test")

    def test_user_can_view_litter(self):
        self.fail("finish the test")

    def test_can_add_cat_to_litter(self):
        self.fail("finish the test")

    def test_can_remove_cats_in_litter(self):
        self.fail("finish the test")

    def test_can_add_events_to_cats_in_litter(self):
        self.fail("finish the test")