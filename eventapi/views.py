from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Event, Location, Organizer

# Create your views here.
class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event