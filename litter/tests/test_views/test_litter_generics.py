from litter.tests.test_views.mixins import *
from django.test import TestCase
from django.urls import reverse
from litter.models import Cat


class TestAllLittersView(BaseTestCaseMixin, TestCase):

    def get_test_case(self):
        return ViewTestCase(
            name="All Litters Test",
            url=reverse('litters'),
            model=None,
            valid_data={},
            redirect_url=None
        )
