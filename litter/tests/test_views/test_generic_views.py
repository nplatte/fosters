from dataclasses import dataclass
from django.db import models
from django.urls import reverse
from litter.models import Cat, Event
from django.test import TestCase
from litter.tests.test_views.mixins import DeleteViewTestCaseMixin, EditViewTestCaseMixin


@dataclass
class AddViewTestCase:
    name: str
    url: str
    model: type[models.Model]
    valid_data: dict
    redirect_url: str

class TestEditCatView(EditViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return AddViewTestCase(
        name="Edit Cat Test",
        url = reverse('edit_cat', kwargs={"pk": 1}),
        model=Cat,
        valid_data={"name": "CAT"},
        redirect_url=reverse("cat", kwargs={"pk": Cat.objects.count()}))


class TestEditEventView(EditViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return AddViewTestCase(
        name="Add Event Test",
        url=reverse('edit_event', kwargs={"pk": 1}),
        model=Event,
        valid_data={"weight": "312", "condition": "super cute", "cat": "1"},
        redirect_url=reverse("cat", kwargs={"pk": Event.objects.count()}))


class TestDeleteCatView(DeleteViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return AddViewTestCase(
        name="Delete Cat",
        url=reverse('delete_cat', kwargs={'pk': Cat.objects.count()}),
        model=Cat,
        valid_data={},
        redirect_url=reverse('all_cats')
    )

class TestDeleteEventView(DeleteViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return AddViewTestCase(
        name="Delete Event",
        url=reverse('delete_event', kwargs={'pk': Event.objects.count()}),
        model=Event,
        valid_data={},
        redirect_url=reverse('all_cats')
    )
