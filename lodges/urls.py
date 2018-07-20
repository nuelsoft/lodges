from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('elements', views.elements, name="elements"),
    path('about', views.about, name="about"),
    path('<int:lodge_id>/details', views.single_listing, name="listing"),
    path('offers', views.offers, name="offers"),
]
