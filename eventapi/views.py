from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpRequest
from django.urls import reverse_lazy

from .models import Event, Location, Organizer
from .forms import EventForm

# Create your views here.
class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    
class EventDeleteView(DeleteView):
    model = Event
    template_name = "eventapi/event_delete.html"
    success_url = reverse_lazy("event-list")