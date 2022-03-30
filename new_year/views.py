import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    today_time = datetime.datetime.now()
    return render(request,"new_year/index.html",{
        "newyear": today_time.day == 1 and today_time.month == 1
    })