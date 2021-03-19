from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TaskForm, UpdateForm
from .models import Task
# Create your views here.

def home_page(request):
    form = TaskForm(request.POST or None)
    tasks = Task.objects.all()
    if form.is_valid():
        Task.objects.create(**form.cleaned_data)
        return redirect("todo:home")

    context = {
        "form" : form,
        "tasks" : tasks,
    }
    return render(request, "index.html", context)

def update_task(request, id):
    obj = Task.objects.get(id=id)
    initial_data = {
        "name" : obj
    }
    form = UpdateForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        name = request.POST["name"]
        newData = Task(id=id, name=name)
        newData.save()
        return redirect("todo:home")
    context = {
        "form" : form,
    }
    return render(request, "update.html", context)

def delete_task(request, id):
    obj = Task.objects.get(id=id)
    obj.delete()
    return redirect("todo:home")