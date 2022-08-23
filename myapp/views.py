from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        print("user loged in")
        return HttpResponse("Hello Geeks")
    else:
        return redirect("login")

def login(request):
    return render(request, "login.html")