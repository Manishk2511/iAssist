from django.shortcuts import render, redirect
from . import views
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from complaints.models import problem, Complaints, latlong
from status.models import status_list, status_type, Complaint_Update
from complaints.forms import ComplaintForm
from government.forms import area_problem_form
from government.models import area_problem_selection, area_available, problem_available
from account.models import User
from django.contrib import messages
from twilio.rest import Client


# from .forms import ComplaintForm
# from .models import problem, complaint
# Create your views here.


def g_home(request):
    if request.user.is_staff:
        return render(request, 'g_home.html')
    else:
        return redirect('/')


def complaint_stats(request):
    return render(request, 'government.html')


# def complaints_list(request):
#     return render(request, 'g_complaints_list.html')

# chart 1

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = problem.objects.all()
        qs1 = status_type.objects.all()

        labels = []
        labels1 = []
        default_items = []
        default_items1 = []

        for item in qs:
            labels.append(item.title)
            value = Complaints.objects.filter(problem_id=item.id).count()
            default_items.append(value)

        for item in qs1:
            labels1.append(item.title)

        # fieldname = 'status'
        # # queryset = status_list.objects.values(fieldname).order_by(
        # #     fieldname).annotate(count=Count(fieldname))
        # default_items1.append(value1)
        for i in range(1, 6):
            value = status_list.objects.filter(status=int(i)).count()
            default_items1.append(value)

        # queryset = status_list.objects.all().annotate(count=Count('status'))
        # for each in queryset:
        #     default_items1.append(each.count)
        #     print(each.count)

        data = {
            "labels": labels,
            "default": default_items,
            "labels1": labels1,
            "default1": default_items1,
        }
        return Response(data)


class AreaChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        Area = area_problem_selection.objects.latest('id').area_selection
        Problem = area_problem_selection.objects.latest('id').problem_selection
        PROBLEM = str(Problem)
        if "All" in PROBLEM:
            qs = problem.objects.all()
        else:
            qs = problem.objects.filter(title=Problem)

        qs1 = status_type.objects.all().order_by('id')

        count = 1
        check = problem.objects.all().order_by('id')
        for item in check:
            if str(item.title) == str(Problem):
                print('worked')
                break
            count += 1

        print(count)
        AREA = str(Area)
        if "All" in AREA:
            if count != 7:
                qs2 = Complaints.objects.filter(problem_id=count)
            else:
                qs2 = Complaints.objects.filter()
        else:
            if count != 7:
                qs2 = Complaints.objects.filter(area=Area, problem_id=count)
            else:
                qs2 = Complaints.objects.filter(area=Area)

        labels = []
        labels1 = []
        default_items = []
        default_items1 = []

        for item in qs:
            if "All" in AREA:
                labels.append(item.title)
                value = Complaints.objects.filter(problem_id=item.id).count()
                default_items.append(value)

            else:
                labels.append(item.title)
                value = Complaints.objects.filter(
                    problem_id=item.id, area=Area).count()
                default_items.append(value)

        for item in qs1:
            labels1.append(item.title)

        # fieldname = 'status'
        # # queryset = status_list.objects.values(fieldname).order_by(
        # #     fieldname).annotate(count=Count(fieldname))
        # default_items1.append(value1)
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for item in qs2:
            l1 = status_list.objects.filter(
                status=1, pk=item.id)
            if len(l1) != 0:
                count1 += 1
            l2 = status_list.objects.filter(
                status=2, pk=item.id)
            if len(l2) != 0:
                count2 += 1
            l3 = status_list.objects.filter(
                status=3, pk=item.id)
            if len(l3) != 0:
                count3 += 1
            l4 = status_list.objects.filter(
                status=4, pk=item.id)
            if len(l4) != 0:
                count4 += 1
            l5 = status_list.objects.filter(
                status=5, pk=item.id)
            if len(l5) != 0:
                count5 += 1

        default_items1.append(count1)
        default_items1.append(count2)
        default_items1.append(count3)
        default_items1.append(count4)
        default_items1.append(count5)

        # value = status_list.objects.filter(status=1,title=Problem).count()
        # default_items1.append(value)
        # value2 = status_list.objects.filter(status=2).count()
        # default_items1.append(value2)
        # queryset = status_list.objects.all().annotate(count=Count('status'))
        # for each in queryset:
        #     default_items1.append(each.count)
        #     print(each.count)

        data = {
            "labels": labels,
            "default": default_items,
            "labels1": labels1,
            "default1": default_items1,
        }
        return Response(data)

# chart 2


# class ChartData1(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         qs1 = status_type.objects.all()

#         labels1 = []
#         default_items1 = []

#         for item in qs1:
#             labels1.append(item.title)
#             value = status_list.objects.filter(status=item.title).count()
#             default_items1.append(value)

#         data = {
#             "labels1": labels1,
#             "default1": default_items1,
#         }
#         return Response(data)


def complaints_list(request):
    no_of_complaints = 6
    page = request.GET.get('pageno')
    MAX = Complaints.objects.all().count()/no_of_complaints

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
    complaints_list = Complaints.objects.all(
    )[no_of_complaints*page-no_of_complaints:no_of_complaints*page]
    status_l = status_list.objects.all()
    status_t = status_type.objects.all()
    done = status_type.objects.get(pk=4)
    return render(request, 'g_complaints_list.html', {'complaints_list': complaints_list, 'status_list': status_l, 'status_type': status_t, 'value': "status", 'prev': prev, 'next': nxt, 'done': done, 'page': page})


# def complaints_form(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = ComplaintForm()
#         return render(request, 'complaints_form.html', {'form': form})


def g_complaints_delete(request, id):
    Complaint = Complaints.objects.get(pk=id)
    Status = status_list.objects.get(pk=id)
    Complaint.delete()
    Status.delete()
    return redirect('g_complaints')


def areaWise(request):
    return render(request, 'area_wise.html')


def area_wise(request):
    if request.method == "GET":
        form = area_problem_form()
        return render(request, 'area_wise.html', {'form': form})
    else:
        form = area_problem_form(request.POST)
        form.save()
        Area = area_problem_selection.objects.latest('id').area_selection
        Problem = area_problem_selection.objects.latest('id').problem_selection
        params = {'area': Area,
                  'problem': Problem}
        if int(request.POST['area_selection']) == 1 and int(request.POST['problem_selection']) == 1:
            return redirect('complaint_stats')
        else:
            return render(request, 'g_area_wise_graph.html', params)

    # return render()


def g_area_wise_graph(request):
    return render(request, 'g_area_wise_graph.html')


def g_map(request):
    location = latlong.objects.all()
    complaints = Complaints.objects.filter(area=request.user.area)
    params = {'locations': location, 'complaints': complaints}
    return render(request, 'g_map.html', params)


def search(request):
    if request.method == 'GET':
        return render(request, 'g_search.html')
    else:
        querry = request.POST['querry']
        if len(querry) > 25:
            result = []
        else:
            if querry.isdigit():
                result = Complaints.objects.filter(id=querry)
            else:
                result1 = Complaints.objects.filter(area__icontains=querry)
                result2 = Complaints.objects.filter(
                    desciption__icontains=querry)
                result = result1.union(result2)

        size = len(result)
        params = {'result': result, 'querry': querry, 'size': size}
        return render(request, 'g_search.html', params)


def g_track_complaint(request, id=0):
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
    return render(request, 'g_track_complaint.html', params)


def g_view_complaint(request, id=0):
    complaint = Complaints.objects.get(id=id)
    image_str = "/media/"+str(complaint.image)
    Time = Complaint_Update.objects.get(complaint_id=id, status_id=5).time
    USER = complaint.user
    user = User.objects.get(pk=USER)
    if user.is_active == False:
        flag = False
    else:
        flag = True
    params = {'complaint': complaint,
              'image_str': image_str, 'flag': flag, 'time': Time}

    return render(request, 'g_view_complaint.html', params)


def block(request, id, c_id):
    user = User.objects.get(pk=id)
    user.is_active = False
    user.save()
    print('done')
    flag = False
    # account_sid = 'AC478afb03a3a7b8ffab8e36d7319254d4'
    # auth_token = '3593f0f7485da298d37e6ac4f5e4cea7'
    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body='You have been blocked by government officer for lodging fake complaint - iAssist',
    #     from_='+14086101214',
    #     to='+917016457155'
    # )
    complaint = Complaints.objects.get(pk=c_id)
    image_str = "/media/"+str(complaint.image)
    params = {'complaint': complaint, 'image_str': image_str, 'flag': flag}
    return render(request, 'g_view_complaint.html', params)


def ratings(request):
    return render(request, 'g_ratings.html', {'value': "ratings"})


def rating_search(request):

    querry = (request.POST['querry']).capitalize()

    if len(querry) > 25 or querry.isdigit():
        result = []
        size = len(result)
        params = {'size': size, 'querry': querry}
        return render(request, 'g_ratings.html', params)
    else:
        result = total_garbage = Complaints.objects.filter(
            area=querry)
        total_garbage = Complaints.objects.filter(
            area=querry, problem_id=1).count()
        garbage_items = Complaints.objects.filter(
            area=querry, problem_id=1)
        count = 0
        for item in garbage_items:
            Status = status_list.objects.filter(pk=item.id, status=4)
            if len(Status) != 0:
                count += 1
        if count > 0:
            garbage_ratio = float(count/total_garbage)*5
        else:
            garbage_ratio = 0

        count = 0
        total_roads = Complaints.objects.filter(
            area=querry, problem_id=2).count()
        road_items = Complaints.objects.filter(
            area=querry, problem_id=2)
        for item in road_items:
            Status = status_list.objects.filter(pk=item.id, status=4)
            if len(Status) != 0:
                count += 1
        if count > 0:
            road_ratio = float(count/total_roads)*5
        else:
            road_ratio = 0

        count = 0
        total_electricity = Complaints.objects.filter(
            area=querry, problem_id=3).count()
        electricity_items = Complaints.objects.filter(
            area=querry, problem_id=3)
        for item in electricity_items:
            Status = status_list.objects.filter(pk=item.id, status=4)
            if len(Status) != 0:
                count += 1
        if count > 0:
            electricity_ratio = float(count/total_electricity)*5
        else:
            electricity_ratio = 0

        count = 0
        total_water = Complaints.objects.filter(
            area=querry, problem_id=4).count()
        water_items = Complaints.objects.filter(
            area=querry, problem_id=4)
        for item in water_items:
            Status = status_list.objects.filter(pk=item.id, status=4)
            if len(Status) != 0:
                count += 1
        if count > 0:
            water_ratio = float(count/total_water)*5
        else:
            water_ratio = 0

        count = 0
        total_education = Complaints.objects.filter(
            area=querry, problem_id=5).count()
        education_items = Complaints.objects.filter(
            area=querry, problem_id=5)
        for item in education_items:
            Status = status_list.objects.filter(pk=item.id, status=4)
            if len(Status) != 0:
                count += 1
        if count > 0:
            education_ratio = float(count/total_education)*5
        else:
            education_ratio = 0

        count = 0
        total_hospital = Complaints.objects.filter(
            area=querry, problem_id=6).count()
        hospital_items = Complaints.objects.filter(
            area=querry, problem_id=6)
        for item in hospital_items:
            Status = status_list.objects.filter(pk=item.id, status=4)
            if len(Status) != 0:
                count += 1
        if count > 0:
            hospital_ratio = float(count/total_hospital)*5

        else:
            hospital_ratio = 0

        avg_rating = round(float((garbage_ratio+hospital_ratio +
                                  education_ratio+electricity_ratio+water_ratio+road_ratio)/5), 2)
        hospital_rating = round(hospital_ratio, 2)
        education_rating = round(education_ratio, 2)
        water_rating = round(water_ratio, 2)
        electricity_rating = round(electricity_ratio, 2)
        road_rating = round(road_ratio, 2)
        garbage_rating = round(garbage_ratio, 2)

        hospital_ratio = hospital_ratio*10*2
        education_ratio = education_ratio*10*2
        water_ratio = water_ratio*10*2
        electricity_ratio = electricity_ratio*10*2
        road_ratio = road_ratio*10*2
        garbage_ratio = garbage_ratio*10*2

        size = len(result)
        params = {'garbage_ratio': garbage_ratio, 'road_ratio': road_ratio, 'hospital_ratio': hospital_ratio,
                  'education_ratio': education_ratio, 'water_ratio': water_ratio, 'electricity_ratio': electricity_ratio, 'size': size,
                  'avg_rating': avg_rating, 'hospital_rating': hospital_rating, 'education_rating': education_rating, 'water_rating': water_rating,
                  'electricity_rating': electricity_rating, 'road_rating': road_rating, 'garbage_rating': garbage_rating, 'querry': querry
                  }
        return render(request, 'g_ratings.html', params)
