from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request:HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('event-list')
    else:
        form  = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})