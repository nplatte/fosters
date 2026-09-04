from litter.tests.test_views.mixins import *
from django.test import TestCase
from django.urls import reverse
from litter.models import Cat


class TestAllCatsView(BaseTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
            name="All Cats Test",
            url=reverse('read_cats')
        )


class TestAddCatView(CreateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Add Cat Test",
        url = reverse('create_cat'),
        model=Cat,
        valid_data={"name": "Cat",
            "estimated_date_of_birth": "01/01/1992",
            "gender": "male", "color": "black",},
        redirect_url=reverse("read_cat", kwargs={"pk": Cat.objects.count()+1}))


class TestEditCatView(UpdateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Edit Cat Test",
        url = reverse('update_cat', kwargs={"pk": 1}),
        model=Cat,
        valid_data={"name": "CAT"},
        redirect_url=reverse("read_cat", kwargs={"pk": Cat.objects.count()}))


class TestDeleteCatView(DeleteViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
        name="Delete Cat",
        url=reverse('delete_cat', kwargs={'pk': Cat.objects.count()}),
        model=Cat,
        valid_data={},
        redirect_url=reverse('read_cats')
    )
