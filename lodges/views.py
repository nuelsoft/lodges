from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import UserProfile, Zone, Lodge
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def elements(request):
    return render(request, 'elements.html')
def index(request):
    return render(request, 'index.html')
def offers(request):
    return render(request, 'offers.html')
def single_listing(request):
    return render(request, 'single_listing.html')
