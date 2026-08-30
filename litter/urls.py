from django.contrib import admin
from django.urls import path, include
from litter.views import *

urlpatterns = [
    path("", LandingView.as_view(), name='landing'),
    path("cat/add", AddCatView.as_view(), name='add_cat'),
    path("cat/edit/<int:pk>", UpdateCatView.as_view(), name='edit_cat')
]