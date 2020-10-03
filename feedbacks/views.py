from django.shortcuts import render, redirect
# from . import views
from .forms import FeedbackForm
from .models import Feedback, problem
# Create your views here.


def feedback(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FeedbackForm()
        else:
            feedback = Feedback.objects.get(pk=id)
            form = FeedbackForm(instance=feedback)
        return render(request, 'feedback_form.html', {'form': form})
    else:
        if id == 0:
            form = FeedbackForm(request.POST)
        else:
            feedback = Feedback.objects.get(pk=id)
            form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
        return redirect('feedback_list')


def feedbackList(request):
    context = {'feedback_list': Feedback.objects.all()}
    return render(request, 'feedback_list.html', context)


def feedbackDelete(request, id):
    feedback = Feedback.objects.get(pk=id)
    feedback.delete()
    return redirect('feedback_list')
