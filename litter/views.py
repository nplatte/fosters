from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from litter.models import *


class LandingView(View):

    def get(self, request):
        return render(request, 'litter/home.html')


class AddCatView(CreateView):

    model = Cat
    fields = ['name', 'estimated_date_of_birth', 'gender', 'color', 'litter']
    template_name = 'litter/cat/add.html'
