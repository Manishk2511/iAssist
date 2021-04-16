from django.shortcuts import render, redirect
from . import views
from django.contrib.auth import logout as django_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib import messages
from twilio.rest import Client
import time
from complaints.models import otp_verification
from django.utils.safestring import mark_safe
import random
# Create your views here.


def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/government')
            else:
                return redirect('/account/otp')
        else:
            messages.error(request, 'Incorrect username or password !')
            return render(request, 'login.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup1.html')
    else:
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        area = request.POST['area']
        city = request.POST['city']
        state = request.POST['state']
        password = request.POST['password']
        r_password = request.POST['r_password']
        USER = get_user_model()
        Username = USER.objects.filter(username=username)
        Email = USER.objects.filter(email=email)
        Phone = USER.objects.filter(contact_no=contact)
        if len(Username) > 0 and len(Email) > 0 and len(Phone) > 0:
            form = request.POST
            messages.error(
                request, 'Username,Email and Contact already exists')
            return render(request, 'signup1.html', {'form': form})
        elif len(Username) > 0 and len(Email) > 0:
            form = request.POST
            messages.error(request, 'Username and Email already exists')
            return render(request, 'signup1.html', {'form': form})
        elif len(Email) > 0 and len(Phone) > 0:
            form = request.POST
            messages.error(request, 'Email and Contact No. already exists')
            return render(request, 'signup1.html', {'form': form})
        elif len(Username) > 0 and len(Phone) > 0:
            form = request.POST
            messages.error(request, 'Username and Contact No. already exists')
            return render(request, 'signup1.html', {'form': form})
        elif len(Username) > 0:
            form = request.POST
            messages.error(request, 'Username already exists')
            return render(request, 'signup1.html', {'form': form})
        elif len(Phone) > 0:
            form = request.POST
            messages.error(request, 'Contact No. already exists')
            return render(request, 'signup1.html', {'form': form})
        elif len(Email) > 0:
            form = request.POST
            messages.error(request, 'Email already exists')
            return render(request, 'signup1.html', {'form': form})

        if password == r_password:
            User = get_user_model()
            user = User.objects.create_user(password=password, username=username, first_name=firstname, last_name=lastname,
                                            email=email, city=city, state=state, area=area, contact_no=contact)
            user.save()
            return redirect('/account/login')
        else:
            messages.error(request, 'Passwords not matched')
            return render(request, 'signup1.html')


def otp(request):
    if request.method == 'GET':
        num = random.randint(11111, 99999)
        print(num)
        # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
        # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #     body=''+str(num)+' is your OTP verification code. -iAssist',
        #     from_='+14086101214',
        #     to='+917016457155'
        # )
        OTP = otp_verification(number=num)
        OTP.save()
        return render(request, 'account_otp.html')
    else:
        num = otp_verification.objects.latest('id')
        number_received = request.POST['first']
        number_received += request.POST['second']
        number_received += request.POST['third']
        number_received += request.POST['fourth']
        number_received += request.POST['fifth']
        if str(num) == str(number_received):
            return redirect('/')
        else:
            messages.error(request, mark_safe(
                '<h3 style="color:#FFCCCB">OTP did not match. Try again </h3>'))
            return redirect('/account/otp')


def logout(request):
    django_logout(request)
    return redirect('/')
