from dataclasses import dataclass
from django.db import models
from django.urls import reverse
from litter.models import Cat


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
    return [
        cat_test_case
    ]