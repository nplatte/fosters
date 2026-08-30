from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from litter.models import *


class LandingView(View):

    def get(self, request):
        return render(request, 'litter/home.html')


class AddCatView(CreateView):

    model = Cat
    fields = ['name', 'estimated_date_of_birth', 'gender', 'color', 'litter']
    template_name = 'litter/cat/add.html'

class UpdateCatView(UpdateView):

    template_name = "litter/cat/edit.html"
    model = Cat
    fields = [
        'name', 'estimated_date_of_birth', 
        'microchip', 'microchip_inserted_on', 'internal_id'
        'gender', 'color', 'litter',
        'is_deleted'
        ]


