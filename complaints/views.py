from django.shortcuts import render, redirect
from . import views
from .forms import ComplaintForm
from .models import problem, complaint
# Create your views here.


def complaints(request):
    return render(request, 'complaints.html')


def complaints_list(request):
    context = {'complaints_list': complaint.objects.all()}
    return render(request, 'complaints_list.html', context)


def complaints_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ComplaintForm()
        else:
            Complaint = complaint.objects.get(pk=id)
            form = ComplaintForm(instance=Complaint)
        return render(request, 'complaints_form.html', {'form': form})
    else:
        if id == 0:
            form = ComplaintForm(request.POST)
        else:
            Complaint = complaint.objects.get(pk=id)
            form = ComplaintForm(request.POST, instance=Complaint)
        if form.is_valid():
            form.save()
        return redirect('list')


def complaints_delete(request, id):
    Complaint = complaint.objects.get(pk=id)
    Complaint.delete()
    return redirect('list')
