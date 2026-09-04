from django.views.generic import CreateView, UpdateView, DeleteView
from litter.models import *
from django.urls import reverse_lazy


class AddEventView(CreateView):

    model = Event
    fields = ['medications', 'weight', 'condition', 'cat']
    template_name = 'litter/generic/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Add Event"
        return context


class UpdateEventView(UpdateView):

    template_name = "litter/generic/edit.html"
    model = Event
    fields = ['medications', 'weight', 'condition', 'cat']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Edit Event"
        return context


class DeleteEventView(DeleteView):

    template_name = "litter/generic/delete.html"
    model = Event

    def get_context_data(self, **kwargs):
        return {
            'title': f"Delete Event"
        }

    def get_success_url(self):
        return  self.object.cat.get_absolute_url()
