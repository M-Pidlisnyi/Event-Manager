from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event-list"),
    path("event/view/<int:pk>", views.EventDetailView.as_view(), name="event-detail"),
    path("event/create", views.EventCreateView.as_view(), name="event-create"),
    path("event/update/<int:pk>", views.EventUpdateView.as_view(), name="event-update"),
    path("event/delete/<int:pk>", views.EventDeleteView.as_view(), name="event-delete"),
    path("visitor/register/", views.register_visitor, name="visitor-register" ),
]
