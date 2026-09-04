from django.views.generic import CreateView, DetailView, ListView, UpdateView
from litter.models import *
from django.urls import reverse_lazy


class AddLitterView(CreateView):

    model = Litter
    fields = ['name']
    template_name = 'litter/generic/add.html'
    success_url = reverse_lazy('litters')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add Litter"
        return context

class AllLittersView(ListView):

    model = Litter
    template_name = 'litter/litter/all.html'


class LitterView(DetailView):

    model = Litter
    template_name = 'litter/litter/detail.html'


class UpdateLitterView(UpdateView):

    model = Litter
    fields = ["name"]
    template_name = 'litter/generic/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Update {kwargs['object'].name}"
        return context
