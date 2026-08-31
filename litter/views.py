from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from litter.models import *
from django.urls import reverse


class LandingView(View):

    def get(self, request):
        return render(request, 'litter/home.html')


class AllCatsView(ListView):

    template_name = 'litter/cat/all.html'

    def get_queryset(self):
        return Cat.objects.all()


class CatView(DetailView):

    model = Cat
    template_name = 'litter/cat/detail.html'


class AddCatView(CreateView):

    model = Cat
    fields = ['name', 'estimated_date_of_birth', 'gender', 'color', 'litter']
    template_name = 'litter/cat/add.html'
    success_url = reverse('landing')

class UpdateCatView(UpdateView):

    template_name = "litter/cat/edit.html"
    model = Cat
    fields = [
        'name', 'estimated_date_of_birth', 
        'microchip', 'microchip_inserted_on', 'internal_id',
        'gender', 'color', 'litter',
        'is_deleted'
        ]


