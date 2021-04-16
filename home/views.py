from django.shortcuts import render, redirect
from complaints.models import Complaints, latlong
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'index.html', {'value': "home"})


def search(request):
    if request.method == 'GET':
        return render(request, 'search.html')
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
        return render(request, 'search.html', params)


# @login_required(login_url="/account/login")
def map(request):

    location = latlong.objects.all()
    complaints = Complaints.objects.filter(area=request.user.area)
    params = {'locations': location, 'complaints': complaints}
    return render(request, 'map.html', params)
