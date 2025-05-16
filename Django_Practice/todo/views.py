from django.shortcuts import render

Tasks = []

# Create your views here.
def todo (request):
    new_task = request.GET('task')
    Tasks = Tasks + new_task
    return render(request, 'index.html', {
        "Tasks": Tasks
    })

def due_task(request):
    return render(request, 'today.html')