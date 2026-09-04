from django.urls import path, include
from litter.views import cat_views as cat_views
from litter.views import litter_views as litter_views
from litter.views import event_views as event_views

urlpatterns = [
    path("", cat_views.LandingView.as_view(), name='landing'),
    path("cat/", include([
        path("add", cat_views.AddCatView.as_view(), name='create_cat'),
        path("view/all", cat_views.AllCatsView.as_view(), name='read_cats'),
        path("view/<int:pk>", cat_views.CatView.as_view(), name='read_cat'),        
        path("edit/<int:pk>", cat_views.UpdateCatView.as_view(), name='update_cat'),
        path("delete/<int:pk>", cat_views.DeleteCatView.as_view(), name='delete_cat')
    ])),
    path("litter/", include([
        path("add", litter_views.AddLitterView.as_view(), name='create_litter'),
        path("view/<int:pk>", litter_views.LitterView.as_view(), name='read_litter'),
        path("view/all", litter_views.AllLittersView.as_view(), name='read_litters'),
        path("edit/<int:pk>", litter_views.UpdateLitterView.as_view(), name='update_litter'),
        path("delete/<int:pk>", litter_views.DeleteLitterView.as_view(), name='delete_litter')
    ])),
    path("event/", include([
        path("add/", event_views.AddEventView.as_view(), name='create_event'), 
        path("edit/<int:pk>", event_views.UpdateEventView.as_view(), name='update_event'), 
        path("delete/<int:pk>", event_views.DeleteEventView.as_view(), name='delete_event')
    ]))
]