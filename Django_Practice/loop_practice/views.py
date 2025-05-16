from django.shortcuts import render

# Create your views here.
def todolist(request):
    tasks = ["read", "eat", "sleep"]
    return render(request, "todo.html", {
        "tasks" : tasks
    })