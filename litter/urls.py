from django.contrib import admin
from django.urls import path, include
from litter.views import *

urlpatterns = [
    path("", LandingPage.as_view(), name='landing')
]