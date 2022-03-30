from django.shortcuts import render

tasks = ["vetorizar", "exercícios de matemática"]

# Create your views here.
def index(request):
    return render(request,'tasks/index.html' ,{
        "tasks": tasks
    })
