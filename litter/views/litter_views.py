from django.views.generic import CreateView, DetailView
from litter.models import *


class AddLitterView(CreateView):

    model = Litter
    fields = ['name']
    template_name = 'litter/litter/add.html'


class LitterView(DetailView):

    model = Litter
    template_name = 'litter/litter/detail.html'