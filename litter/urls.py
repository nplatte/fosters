from django.contrib import admin
from django.urls import path, include
from litter.views import *

urlpatterns = [
    path("", LandingView.as_view(), name='landing'),
    path("cat/", include([
        path("add", AddCatView.as_view(), name='add_cat'),
        path("edit/<int:pk>", UpdateCatView.as_view(), name='edit_cat'),
        path("view/all", AllCatsView.as_view(), name='all_cats'),
        path("view/<int:pk>", CatView.as_view(), name='cat')
    ]))
]