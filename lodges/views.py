from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import UserProfile, Zone, Lodge
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def news(request):
    return HttpResponse("This is The news Page.")
def elements(request):
    return HttpResponse("This is The elements Page.")
def listings(request):
    return render(request, 'listings.html')
def listings_single(request):
    return HttpResponse("This is The Single listings Page.")
def about(request):
    return render(request, 'about.html')
