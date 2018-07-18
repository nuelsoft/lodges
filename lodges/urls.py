from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="login"),
    path('signup', views.signup, name="signup"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboard/<str:zone_name>', views.zone, name="zone"),
]
