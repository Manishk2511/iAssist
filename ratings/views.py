from django.shortcuts import render
from . import views
from complaints.models import Complaints
from status.models import status_list
# Create your views here.


def ratings(request):
    return render(request, 'ratings.html', {'value': "ratings"})


def search(request):

    querry = (request.POST['querry']).capitalize()

    if len(querry) > 25 or querry.isdigit():
        result = []
        size = len(result)
        params = {'size': size, 'querry': querry}
        return render(request, 'ratings.html', params)
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
        return render(request, 'ratings.html', params)
