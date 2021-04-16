from django.shortcuts import render, redirect
from . import views
from .models import status_list, Complaint_Update, status_type, user_status_type, user_status_list
from .forms import status_form, user_status_form
from twilio.rest import Client
import time
# Create your views here.


#
def status(request):
    return render(request, 'status.html')


def status_update(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = status_form(initial={'customer_id': id})
        else:
            pass
            try:
                Status = status_list.objects.get(complaint_id=id)
            except status_list.DoesNotExist:
                Status = None
            form = user_status_form(initial={'customer_id': id})
        return render(request, 'status.html', {'value': "status", 'form': form, 'id': id})
    else:
        if id == 0:
            form = user_status_form(request.POST)
        else:
            # try:
            #     Status = status_list.objects.get(complaint_id=id)
            # except status_list.DoesNotExist:
            #     Status = None
            # Status = status_list.objects.get(complaint_id=id)
            # request.POST.complaint_id_id = id
            s = status_list(complaint_id=id,
                            status_id=request.POST['status'])
            s.save()
            Status = status_list.objects.get(complaint_id=id).status
            Status1 = status_type.objects.get(pk=3).title
            Status2 = status_type.objects.get(pk=4).title

            if str(Status) == Status1:
                update = Complaint_Update(
                    complaint_id=id, desc="Complaint is under process and Work is initiated for the complaint", status=Status)
                update.save()

                # uncomment this......................................IMP..............................

                # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
                # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
                # client = Client(account_sid, auth_token)

                # message = client.messages.create(
                #     body='Complaint ' +
                #     str(update.complaint_id)+' is kept under process at :' +
                #     str(update.time)+' - iAssist',
                #     from_='+14086101214',
                #     to='+917016457155'
                # )

            elif str(Status) == Status2:
                update = Complaint_Update(
                    complaint_id=id, desc="Comlaint is solved", status=Status)
                update.save()

                # uncomment this......................................IMP..............................

                # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
                # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
                # client = Client(account_sid, auth_token)

                # message = client.messages.create(
                #     body='Complaint ' +
                #     str(update.complaint_id)+' is solved. Work was completed at :' +
                #     str(update.time)+' - iAssist',
                #     from_='+14086101214',
                #     to='+917016457155'
                # )
            # form = status_form(request.POST)
            # var = form['complaint_id']
            # # if form.is_valid():
            # form.save()

            return redirect('list')


def g_status_update(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = status_form(initial={'customer_id': id})
        else:
            pass
            try:
                Status = status_list.objects.get(complaint_id=id)
            except status_list.DoesNotExist:
                Status = None
            form = status_form(initial={'customer_id': id})
        return render(request, 'g_status.html', {'value': "status", 'form': form, 'id': id})
    else:
        if id == 0:
            form = status_form(request.POST)
        else:
            # try:
            #     Status = status_list.objects.get(complaint_id=id)
            # except status_list.DoesNotExist:
            #     Status = None
            # Status = status_list.objects.get(complaint_id=id)
            # request.POST.complaint_id_id = id
            s = status_list(complaint_id=id,
                            status_id=request.POST['status'])
            s.save()

            Status = status_list.objects.get(complaint_id=id).status
            Status1 = status_type.objects.get(pk=2).title
            Status2 = status_type.objects.get(pk=3).title
            Status3 = status_type.objects.get(pk=4).title

            if str(Status) == Status1:
                update = Complaint_Update(
                    complaint_id=id, desc="complaint has been Approved by the authority", status=Status)
                update.save()

                # uncomment this......................................IMP..............................

                # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
                # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
                # client = Client(account_sid, auth_token)

                # message = client.messages.create(
                #     body='Complaint ' +
                #     str(update.complaint_id)+' Approved by Authority at :' +
                #     str(update.time)+' -iAssist',
                #     from_='+14086101214',
                #     to='+917016457155'
                # )

            elif str(Status) == Status2:
                update = Complaint_Update(
                    complaint_id=id, desc="Complaint is under process and Work is initiated for the complaint", status=Status)
                update.save()

                # uncomment this......................................IMP..............................

                # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
                # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
                # client = Client(account_sid, auth_token)

                # message = client.messages.create(
                #     body='Complaint ' +
                #     str(update.complaint_id)+' is kept under process at :' +
                #     str(update.time)+' - iAssist',
                #     from_='+14086101214',
                #     to='+917016457155'
                # )

            elif str(Status) == Status3:
                update = Complaint_Update(
                    complaint_id=id, desc="Comlaint is solved", status=Status)
                update.save()

                # uncomment this......................................IMP..............................

                # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
                # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
                # client = Client(account_sid, auth_token)

                # message = client.messages.create(
                #     body='Complaint ' +
                #     str(update.complaint_id)+' is solved. Work was completed at :' +
                #     str(update.time)+' - iAssist',
                #     from_='+14086101214',
                #     to='+917016457155'
                # )
            # form = status_form(request.POST)
            # var = form['complaint_id']
            # # if form.is_valid():
            # form.save()

            return redirect('g_complaints')


# def complaints_form(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = ComplaintForm()
#         else:
#             Complaint = complaint.objects.get(pk=id)
#             form = ComplaintForm(instance=Complaint)
#         return render(request, 'complaints_form.html', {'form': form})
#     else:
#         if id == 0:
#             form = ComplaintForm(request.POST)
#         else:
#             Complaint = complaint.objects.get(pk=id)
#             form = ComplaintForm(request.POST, instance=Complaint)
#         if form.is_valid():
#             form.save()
#         return redirect('list')
