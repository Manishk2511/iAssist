from django.shortcuts import render
from . import views
# Create your views here.


def status(request):
    return render(request, 'status.html', {'value': "status"})
