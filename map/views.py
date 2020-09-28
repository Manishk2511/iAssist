from django.shortcuts import render
from . import views
# Create your views here.


def map(request):
    return render(request, 'map.html', {'value': "map"})
