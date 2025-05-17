from django.shortcuts import render
from dataclasses import dataclass
import datetime 

@dataclass
class task():
    name: str
    date: str
    time: str


Tasks = []

# Create your views here.
def todo (request):
    if request.method == "GET":
        return render (request, 'index.html')
        
    if request.method == "POST":
        new_task = task(request.POST['task'].capitalize(), request.POST['Due-date'], request.POST['Due-time'])
        Tasks.append(new_task)
        return render(request, 'index.html', {
        "Tasks" : Tasks,
        })

def due_task(request):
    Due_Tasks = []
    for task in Tasks:
        date = task.date.split("-")
        today = datetime.date.today()
        if int(date[0]) == int(today.year) and int(date[1]) == int(today.month) and int(date[2]) == int(today.day):
            Due_Tasks.append(task)
    Due_Tasks        
    return render(request, 'today.html', {
        "Due_Tasks" : Due_Tasks
    })