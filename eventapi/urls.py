from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event-list"),
    path("event/view/<int:pk>", views.EventDetailView.as_view(), name="event-detail")

]
