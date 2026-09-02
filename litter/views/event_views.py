from django.views.generic import CreateView, DetailView
from litter.models import *


class AddEventView(CreateView):

    model = Event
    fields = ['medications', 'weight', 'condition', 'cat']
    template_name = 'litter/generic/add.html'

    def get_context_data(self, **kwargs):
        return {
            "title": "Add Event"
        }