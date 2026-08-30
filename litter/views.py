from django.shortcuts import render
from django.views import View


class LandingView(View):

    def get(self, request):
        return render(request, 'litter/home.html')


class AddCatView(View):

    def get(self, request):
        return render(request, 'litter/cat/add.html')
