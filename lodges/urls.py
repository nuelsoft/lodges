from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('news', views.news, name="news"),
    path('elements', views.elements, name="elements"),
    path('about', views.about, name="about"),
    path('listings', views.listings, name="listings"),
    path('listings_single', views.listings_single, name="listings_single"),
]
