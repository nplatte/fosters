from django.urls import reverse
from litter.models import Cat, Event
from functional_tests.foster_helper import TestHelper


class TestEvent(TestHelper):

    fixtures = [ "cats", "events" ]

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
        cat = Cat.objects.get(pk=1)
        # the user logs into the website
        self.log_in_to_site()
        # the user goes to the all cats page
        self.navigate_to_cats_page()
        # the user clicks on the cat with an event
        self.find_and_click(f"view_{cat.pk}_link")
        # they see events
        got = self.count_elements_by_class("event")
        cat_events = Event.objects.filter(cat=cat)
        self.assertEqual(len(cat_events), got)
        # they see the events info
        event = cat_events.first()
        for field, data in {"meds":event.medications, "weight":f"{event.weight} grams", "condition":event.condition}.items():
            element = self.findElementByID(f"event_{event.pk}_{field}")
            self.assertEqual(element.text, data)

    def test_edit_event(self):
        cat = Cat.objects.get(pk=1)
        # the user logs into the website
        self.log_in_to_site()
        # the user goes to the all cats page
        self.navigate_to_cats_page()
        # the user clicks on the cat with an event
        self.find_and_click(f"view_{cat.pk}_link")
        self.assertTitleEquals(cat.name)
        # they see events
        count = self.count_elements_by_class("event")
        self.assertGreater(count, 0)
        event_weight = self.findElementByID("event_1_weight")
        self.assertNotEqual(event_weight.text, "200 grams")
        # they click the event edit button
        self.find_and_click("event_1_edit")
        self.assertTitleEquals("Edit Event")
        # they update the weight
        data = {"weight": "200"}
        self.fill_in_form_by_ids(data)
        # they are taken to the cat page again
        self.assertTitleEquals(cat.name)
        # they see the event weight is updated
        event_weight = self.findElementByID("event_1_weight")
        self.assertEqual(event_weight.text, "200 grams")

    def test_delete_event(self):
        cat = Cat.objects.get(pk=1)
        # the user logs into the page
        self.log_in_to_site()
        # the user goes to the cats page
        self.navigate_to_cats_page()
        # they click a cat
        self.find_and_click("view_1_link")
        self.assertTitleEquals(cat.name)
        # they see the event they want to delete
        event_count = self.count_elements_by_class("event")
        self.assertGreater(event_count, 0)
        self.find_and_click("event_1_delete")
        # they are taken to a new page
        self.assertTitleEquals("Delete Event")
        # they click the submit button 
        self.find_and_click("submit-btn")
        # they are taken back to the cat page
        self.assertTitleEquals(cat.name)
        # they see less events
        new_count = self.count_elements_by_class("event")
        self.assertLess(new_count, event_count)

