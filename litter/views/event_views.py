from django.views.generic import CreateView, DetailView
from litter.models import *


class AddEventView(CreateView):

    model = Litter
    fields = ['name']
    template_name = 'litter/litter/add.html'