from django.views.generic import CreateView
from litter.models import *


class AddLitterView(CreateView):

    model = Cat
    fields = ['name']
    template_name = 'litter/litter/add.html'