import time
from django.shortcuts import render


# Create your views here.

#Renders default hello page
def hello (request):
    return render(request, "greetings.html", {
        "name": "World"
    })

#Renders greetings with name
def greetings (request, name):
    return render(request, "greetings.html", {
        "name": name.capitalize()
    })

#Checks if today is 5th April and returns whether today is my birthday or not with conditional logic in views.py
def birthday_v1 (request):
    date = time.ctime().split()
    #Checks if the date is 5th April
    if date[2] == "5" and date[1] == "April":
        return render(request, "birthday_v1.html", {
            "state": "Yes",
            "state_use": ""
        })
    else:
        return render(request, "birthday_v1.html", {
            "state": "No",
            "state_use": "not"
        })
    

#Checks if today is 5th April and returns whether today is my birthday or not with conditional logic in the Html file
def birthday_v2(request):
    date = time.ctime().split()
    return render (request, "birthday_v2.html", {
        "birthday": date[2] == "5" and date[1] == "April"
    })

