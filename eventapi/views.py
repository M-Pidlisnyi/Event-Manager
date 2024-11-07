from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpRequest, HttpResponseBadRequest
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event, Location, Organizer, Visitor
from .forms import EventForm, CreateVisitorForm
from .mixins import UserIsOwnerMixin

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    form_class = EventForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EventUpdateView(UserIsOwnerMixin, LoginRequiredMixin,UpdateView):
    model = Event
    form_class = EventForm
    
class EventDeleteView(UserIsOwnerMixin, LoginRequiredMixin,DeleteView):
    model = Event
    template_name = "eventapi/event_delete.html"
    success_url = reverse_lazy("event-list")

    
def register_visitor(request:HttpRequest):
    form = CreateVisitorForm()
    event_id = ""
    if request.method == "GET":
        event_id = request.GET.get("event_id", False)
        if not event_id:
            return HttpResponseBadRequest("400 No event id provided") 
        
        if request.GET.get("self", ""):
            form.initial["first_name"] = request.user.first_name
            form.initial["last_name"] = request.user.last_name
            form.initial["contact_email"] = request.user.email

        form.initial["event_id"] = int(event_id)

    elif request.method == "POST":
        form = CreateVisitorForm(request.POST)

        if form.is_valid():
            event_id = form.cleaned_data["event_id"]
            event = Event.objects.get(id=int(event_id))
           
            visitor:Visitor = form.save(commit=False)
            visitor.user = request.user
            visitor.save()

            visitor.events.add(event)

            return redirect(reverse("event-detail", kwargs={"pk": int(event_id)}))

    return render(request,"eventapi/register_visitor.html", {"form":form})