from django import forms
from .models import Event,Visitor

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Event
        fields = "__all__"
        exclude = ("user",)

class CreateVisitorForm(forms.ModelForm):

    event_id  = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Visitor
        fields = ("first_name", "last_name", "contact_email", "contact_phone")
   