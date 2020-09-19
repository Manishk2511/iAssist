from django.shortcuts import render
from . import views
# Create your views here.


def ratings(request):
    return render(request, 'ratings.html')
