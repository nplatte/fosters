from litter.tests.test_views.mixins import *
from django.test import TestCase
from django.urls import reverse
from litter.models import Litter


class TestAllLittersView(BaseTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
            name="All Litters Test",
            url=reverse('litters'),
            model=None,
            valid_data={},
            redirect_url=None
        )

class TestAddLitterView(CreateViewTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
            name="Add Litters Test",
            url=reverse('add_litter'),
            model=Litter,
            valid_data={"name": "test 123"},
            redirect_url=reverse('litters')
        )
