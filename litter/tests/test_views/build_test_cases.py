from dataclasses import dataclass
from django.db import models
from django.urls import reverse
from litter.models import Cat, Event


@dataclass
class AddViewTestCase:
    name: str
    url: str
    model: type[models.Model]
    valid_data: dict
    redirect_url: str


def build_add_view_test_cases():
    cat_test_case = AddViewTestCase(
        name="Add Cat Test",
        url = reverse('add_cat'),
        model=Cat,
        valid_data={"name": "Cat",
            "estimated_date_of_birth": "01/01/1992",
            "gender": "male", "color": "black",},
        redirect_url=reverse("cat", kwargs={"pk": Cat.objects.count()+1}))

    event_test_case = AddViewTestCase(
        name="Add Event Test",
        url=reverse('add_event'),
        model=Event,
        valid_data={"medications": "Clab, Blab, Rave",
            "weight": "123", "condition": "super cute", "cat":f"{Cat.objects.count()+1}"},
        redirect_url=reverse("cat", kwargs={"pk": Cat.objects.count()+1}))
    
    return [
        cat_test_case, event_test_case
    ]


def build_edit_view_test_cases():
    cat_test_case = AddViewTestCase(
        name="Edit Cat Test",
        url = reverse('edit_cat', kwargs={"pk": 1}),
        model=Cat,
        valid_data={"name": "CAT"},
        redirect_url=reverse("cat", kwargs={"pk": Cat.objects.count()}))

    event_test_case = AddViewTestCase(
        name="Add Event Test",
        url=reverse('edit_event', kwargs={"pk": 1}),
        model=Event,
        valid_data={"weight": "312", "condition": "super cute", "cat": "1"},
        redirect_url=reverse("cat", kwargs={"pk": Event.objects.count()}))
    
    return [
        cat_test_case, event_test_case
    ]


def build_delete_view_test_cases():
    cat_test_case = AddViewTestCase(
        name="Delete Cat",
        url=reverse('delete_cat', kwargs={'pk': Cat.objects.count()}),
        model=Cat,
        valid_data={},
        redirect_url=reverse('all_cats')
    )
    event_test_case = AddViewTestCase(
        name="Delete Event",
        url=reverse('delete_event', kwargs={'pk': Event.objects.count()}),
        model=Event,
        valid_data={},
        redirect_url=reverse('cat', kwargs={'pk': Cat.objects.count()})
    )
    return [ cat_test_case, event_test_case ]
