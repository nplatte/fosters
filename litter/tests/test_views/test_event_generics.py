from django.urls import reverse
from litter.models import Cat, Event
from django.test import TestCase
from litter.tests.test_views.mixins import *

class TestAddEventView(CreateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Add Event Test",
        url=reverse('add_event'),
        model=Event,
        valid_data={"medications": "Clab, Blab, Rave",
            "weight": "123", "condition": "super cute", "cat":1},
        redirect_url=reverse("read_cat", kwargs={"pk": 1}))


class TestEditEventView(UpdateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Add Event Test",
        url=reverse('edit_event', kwargs={"pk": 1}),
        model=Event,
        valid_data={"weight": "312", "condition": "super cute", "cat": "1"},
        redirect_url=reverse("read_cat", kwargs={"pk": Event.objects.count()}))


class TestDeleteEventView(DeleteViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Delete Event",
        url=reverse('delete_event', kwargs={'pk': Event.objects.count()}),
        model=Event,
        valid_data={},
        redirect_url=reverse("read_cat", kwargs={"pk": 1})
    )
