from dataclasses import dataclass
from django.db import models
from django.urls import reverse
from litter.models import Cat, Event
from django.test import TestCase
from litter.tests.test_views.mixins import DeleteViewTestCaseMixin, UpdateViewTestCaseMixin, CreateViewTestCaseMixin


@dataclass
class ViewTestCase:
    name: str
    url: str
    model: type[models.Model]
    valid_data: dict
    redirect_url: str


class TestAddCatView(CreateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Add Cat Test",
        url = reverse('add_cat'),
        model=Cat,
        valid_data={"name": "Cat",
            "estimated_date_of_birth": "01/01/1992",
            "gender": "male", "color": "black",},
        redirect_url=reverse("cat", kwargs={"pk": Cat.objects.count()+1}))


class TestAddEventView(CreateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Add Event Test",
        url=reverse('add_event'),
        model=Event,
        valid_data={"medications": "Clab, Blab, Rave",
            "weight": "123", "condition": "super cute", "cat":1},
        redirect_url=reverse("cat", kwargs={"pk": 1}))


class TestEditCatView(UpdateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Edit Cat Test",
        url = reverse('edit_cat', kwargs={"pk": 1}),
        model=Cat,
        valid_data={"name": "CAT"},
        redirect_url=reverse("cat", kwargs={"pk": Cat.objects.count()}))


class TestEditEventView(UpdateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Add Event Test",
        url=reverse('edit_event', kwargs={"pk": 1}),
        model=Event,
        valid_data={"weight": "312", "condition": "super cute", "cat": "1"},
        redirect_url=reverse("cat", kwargs={"pk": Event.objects.count()}))


class TestDeleteCatView(DeleteViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Delete Cat",
        url=reverse('delete_cat', kwargs={'pk': Cat.objects.count()}),
        model=Cat,
        valid_data={},
        redirect_url=reverse('all_cats')
    )


class TestDeleteEventView(DeleteViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Delete Event",
        url=reverse('delete_event', kwargs={'pk': Event.objects.count()}),
        model=Event,
        valid_data={},
        redirect_url=reverse('all_cats')
    )
