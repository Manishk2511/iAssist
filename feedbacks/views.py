from django.shortcuts import render, redirect
# from . import views
from .forms import FeedbackForm
from .models import Feedback_list, problem
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/account/login')
def feedback(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FeedbackForm()
        else:
            feedback = Feedback_list.objects.get(pk=id)
            form = FeedbackForm(instance=feedback)
        return render(request, 'feedback_form.html', {'form': form, 'value': "feedback"})
    else:
        if id == 0:
            form = FeedbackForm(request.POST)
        else:
            feedback = Feedback_list.objects.get(pk=id)
            form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
        return redirect('feedback_list')


def feedbackList(request):
    feedback_list = Feedback_list.objects.all()
    return render(request, 'feedback_list.html', {'value': "feedback", 'feedback_list': feedback_list})


def feedbackDelete(request, id):
    feedback = Feedback_list.objects.get(pk=id)
    feedback.delete()
    return redirect('feedback_list')
