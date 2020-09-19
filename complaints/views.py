from django.shortcuts import render
from . import views

# Create your views here.


def complaints(request):
    return render(request, 'complaints.html')
