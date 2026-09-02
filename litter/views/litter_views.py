from django.views.generic import CreateView, DetailView
from litter.models import *


class AddLitterView(CreateView):

    model = Litter
    fields = ['name']
    template_name = 'litter/generic/add.html'

    def get_context_data(self, **kwargs):
        return {
            "title": "Add Event"
        }


class LitterView(DetailView):

    model = Litter
    template_name = 'litter/litter/detail.html'