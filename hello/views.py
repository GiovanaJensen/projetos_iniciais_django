from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def greet(request, name):
    return render(request,"hello/greet.html",{
        "name": name.capitalize()
    })

def champs(request):
    return render(request,"hello/champions.html",{
        "conference_champs": ["California","Utah","Oregon State", "Arizona State","UCLA","Washington","Stanford","Arizona"]
    })