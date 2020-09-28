from django.shortcuts import render
from . import views
# Create your views here.


def stats(request):
    return render(request, 'statistics.html', {'value': "stats"})
