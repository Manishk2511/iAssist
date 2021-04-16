from django.shortcuts import render, redirect
from . import views
from .forms import ComplaintForm, ImageForm
from .models import problem, Complaints, otp_verification, image_upload, latlong
from status.models import status_list, status_type, Complaint_Update
from pathlib import Path, os
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe

from twilio.rest import Client
import time
import random
from django.contrib import messages
from django.contrib.gis.geoip2 import GeoIP2
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


# Create your views here.


def complaints(request):
    return render(request, 'complaints.html')


@login_required(login_url='/account/login')
def complaints_list(request):
    no_of_complaints = 6
    page = request.GET.get('pageno')
    MAX = Complaints.objects.filter(
        user=request.user.id).count()/no_of_complaints

    # print(page)
    if page is None:
        page = 1
    else:
        page = int(page)
    # print(page)
    if page > 1:
        prev = page-1
    else:
        prev = None

    if page < MAX:
        nxt = page+1
    else:
        nxt = None
    complaints_list = Complaints.objects.filter(user=request.user.id
                                                )[no_of_complaints*page-no_of_complaints:no_of_complaints*page]
    status_l = status_list.objects.all()
    status_t = status_type.objects.all()
    allowed = status_type.objects.get(pk=5)
    done = status_type.objects.get(pk=4)
    return render(request, 'complaints_list.html', {'complaints_list': complaints_list, 'status_list': status_l, 'status_type': status_t, 'value': "status", 'prev': prev, 'next': nxt, 'allowed': allowed, 'done': done, 'page': page})


@login_required(login_url='/account/login')
def complaints_form(request, id=0):
    # if request.user.is_authenticated:

    if request.method == "GET":
        if id == 0:
            # form1 = ImageForm()
            form = ComplaintForm()
        else:
            # Image = image_upload.objects.get(pk=id)
            Complaint = Complaints.objects.get(pk=id)
            form = ComplaintForm(instance=Complaint)
            # form1 = ImageForm(instance=Image)
        return render(request, 'complaints_form.html', {'form': form})
    else:
        if id == 0:
            Image.init()
            form = ComplaintForm(request.POST, request.FILES)
            path = request.FILES['image']
            path_name = "media/img/"+str(path)
            meta_data = ImageMetaData(path_name)
            latlng = meta_data.get_lat_lng()
            if (latlng[0]):
                if form.is_valid():
                    # form.save()
                    # print('working')
                    Problem = problem.objects.get(id=request.POST['problem'])
                    complaint = Complaints(problem=Problem, desciption=request.POST['desciption'],
                                           area=(request.POST['area']).capitalize(), pincode=request.POST['pincode'], image=request.FILES['image'], user=request.user.id)
                    complaint.save()
                    obj = Complaints.objects.latest('id').id
                    s = status_list(complaint_id=obj,
                                    status_id=5)
                    s.save()
                    # form1 = ImageForm(request.POST, request.FILES)
                    # form1.save()
                    # if form1.is_valid():
                    #     Image.save()
                    #     form1.save()
                    # else:
                    #     print('not saved')
                    # Image = image_upload(
                    #     complaint_id=obj, image=request.FILES['image'].read())
                    # Image.save()

                    Status = status_list.objects.get(complaint_id=obj).status
                    update = Complaint_Update(
                        complaint_id=obj, desc="complaint is been registered", status=Status)
                    update.save()
                    TIME = update.time
                    location = latlong(
                        complaint_id=obj, latitude=latlng[0], longitude=latlng[1])
                    location.save()
                    print(latlng)
                    # sending sms

                    # uncomment this......................................IMP..............................

                    # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
                    # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
                    # client = Client(account_sid, auth_token)

                    # message = client.messages.create(
                    #     body='Complaint ' +
                    #     str(obj)+' registered at :'+str(TIME)+' -iAssist',
                    #     from_='+14086101214',
                    #     to='+917016457155'
                    # )

            else:
                form = ComplaintForm(request.POST, request.FILES)
                messages.error(
                    request, mark_safe('<h4>GPS location not found in image.</h4> <h5><b>Suggestion</b> : First turn on gps and then click picture</h5>'))
                return render(request, 'complaints_form.html', {'form': form})

        else:
            Complaint = Complaints.objects.get(pk=id)
            form = ComplaintForm(request.POST, instance=Complaint)
            if form.is_valid():
                form.save()

        return redirect('otp')
    # else:
    #     return redirect('login')


def complaints_delete(request, id):
    Complaint = Complaints.objects.get(pk=id)
    Status = status_list.objects.get(pk=id)
    Complaint.delete()
    Status.delete()
    return redirect('list')


def track_complaint(request, id=0):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    # # ip = request.META.get('REMOTE_ADDR')
    # print(ip)
    # IP = '2405:204:8589:8c13:183c:4461:a8a9:14a8'
    # g = GeoIP2()
    # lat, lng = g.lat_lon(IP)
    # print(lat)
    # print(lng)
    # path_name = "statics/IMG_20210317_201849.jpg"
    # meta_data = ImageMetaData(path_name)
    # latlng = meta_data.get_lat_lng()
    # print(latlng)
    # exif_data = meta_data.get_exif_data()
    # print(exif_data)
    Complaint = Complaints.objects.get(pk=id)
    update = Complaint_Update.objects.filter(complaint_id=id)
    params = {
        'complaint': Complaint,
        'update': update,
        'id': id,
    }
    return render(request, 'track_complaint.html', params)


@login_required(login_url='/account/login')
def view_complaint(request, id=0):
    # if request.user.is_authenticated:
    Time = Complaint_Update.objects.get(complaint_id=id, status_id=5).time
    complaint = Complaints.objects.get(id=id)
    image_str = "/media/"+str(complaint.image)
    params = {'complaint': complaint, 'image_str': image_str, 'time': Time}

    return render(request, 'view_complaint.html', params)

    # else:
    #     return redirect('login')


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
        return render(request, 'otp.html')
    else:
        num = otp_verification.objects.latest('id')
        number_received = request.POST['otp']
        if str(num) == str(number_received):
            return redirect('list')
        else:
            messages.error(request, 'Otp didnt matched. Try again')
            return redirect('/complaints/otp')


def view_on_map(request, id):
    complaint = Complaints.objects.get(pk=id)
    latitude = latlong.objects.filter(
        complaint_id=id).values_list('latitude', flat=True).order_by('complaint_id')
    longitude = latlong.objects.filter(
        complaint_id=id).values_list('longitude', flat=True).order_by('complaint_id')
    latitude = str(latitude)
    longitude = str(longitude)
    lats = ''
    longs = ''
    for i in latitude:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            lats += i

    for i in longitude:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            longs += i

    params = {'complaint': complaint,
              'latitude': lats, 'longitude': longs}
    return render(request, 'view_on_map.html', params)


class ImageMetaData(object):
    '''
    Extract the exif data from any image. Data includes GPS coordinates, 
    Focal Length, Manufacture, and more.
    '''
    exif_data = None
    image = None

    def __init__(self, img_path):
        self.image = Image.open(img_path)
        # print(self.image._getexif())
        self.get_exif_data()
        super(ImageMetaData, self).__init__()

    def get_exif_data(self):
        """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
        exif_data = {}
        info = self.image._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]

                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value
        self.exif_data = exif_data
        return exif_data

    def get_if_exist(self, data, key):
        if key in data:
            return data[key]
        return None

    def convert_to_degress(self, value):
        """Helper function to convert the GPS coordinates 
        stored in the EXIF to degress in float format"""
        degrees = value[0]
        minutes = value[1] / 60.0
        seconds = value[2] / 3600.0
        return degrees + minutes + seconds

    def get_lat_lng(self):
        """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
        lat = None
        lng = None
        exif_data = self.get_exif_data()
        # print(exif_data)
        if "GPSInfo" in exif_data:
            gps_info = exif_data["GPSInfo"]
            gps_latitude = self.get_if_exist(gps_info, "GPSLatitude")
            gps_latitude_ref = self.get_if_exist(gps_info, 'GPSLatitudeRef')
            gps_longitude = self.get_if_exist(gps_info, 'GPSLongitude')
            gps_longitude_ref = self.get_if_exist(gps_info, 'GPSLongitudeRef')
            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = self.convert_to_degress(gps_latitude)
                if gps_latitude_ref != "N":
                    lat = 0 - lat
                lng = self.convert_to_degress(gps_longitude)
                if gps_longitude_ref != "E":
                    lng = 0 - lng
        return lat, lng
