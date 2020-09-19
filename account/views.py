from django.shortcuts import render
from . import views

# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
