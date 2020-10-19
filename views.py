from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render
from myapp.models import Task


def home(request):
    return render(request, 'home.html')


def index(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(note_title=title, note_description=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Task.objects.all()
    print(allTasks)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)
