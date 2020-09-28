from django.shortcuts import render
from . import views
# Create your views here.


def feedback(request):
    return render(request, 'feedback.html', {'value': "feedback"})
