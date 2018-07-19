from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('elements', views.elements, name="elements"),
    path('about', views.about, name="about"),
    path('single_listing', views.single_listing, name="single_listing"),
    path('offers', views.offers, name="offers"),
]
