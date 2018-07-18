from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import UserProfile, Zone, Lodge
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse(dashboard))
        else:
            return HttpResponseRedirect(reverse(login))

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        name = request.POST["name"]
        phone = request.POST["phone"]
        department = request.POST["department"]
        faculty = request.POST["faculty"]
        level = request.POST["level"]
        gender = request.POST["gender"]
        study = request.POST["study"]
        kin_name = request.POST["kin"]
        kin_phone = request.POST["kin_phone"]
        self_description = request.POST["description"]

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        userProfile = UserProfile(user=user, full_name=name, phone=phone, department=department, faculty=faculty,level=level, gender=gender, study=study, kin_name=kin_name, kin_phone=kin_phone, self_description=self_description)
        userProfile.save()
        return HttpResponse("""<h1>You have successfully registered</h1><br><p>Click <a href="{% url 'login' %}">here</a> to login</p>""")

    return render(request, 'signup.html')

def dashboard(request):
    user = request.user
    if not user:
        return HttpResponseRedirect(reverse(login))
    context = {
        "p" : UserProfile.objects.get(user=User.objects.get(username=user)),
        "zones" : Zone.objects.all(),
    }
    return render(request, 'dashboard.html', context)

def zone(request, zone_name):
    try:
        Zone.objects.get(name=zone_name.capitalize())
    except Zone.DoesNotExist:
        return Http404("Selected Zone does not exist.")
    return HttpResponse("Correct Zone!!")
