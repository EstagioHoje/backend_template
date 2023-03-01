from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
import json
from django.core import serializers

# Create your views here.

# Create a task
def task_create(request):
    print(f"request = {request}")
    form = TaskForm(request)
    form.save()
    # return HttpResponse(str(request.POST))
    if request.method == "POST":
        print(f"request.POST = {request.POST}")
        print(f"request.query_params = {request.query_params}")
        form = TaskForm(request.POST)
        print(f"form = {form}")
        if form.is_valid():
            form.save()
            return redirect(reverse(":task_list"))
        else:
            print(f"form.errors = {form.errors}")
    else:
        form = TaskForm()

    return HttpResponse('task criada!')
    # return render(request, "tasks/task_form.html", { "form": form, })


# Retrieve task list
def task_list(request):

    queryset = serializers.serialize("json",Task.objects.all())
    context = {
        'queryset': queryset
    }
    context = json.dumps(queryset, default=str)
    return HttpResponse(context)
    # queryset = Task.objects.all()
    # context ={
    #     'queryset': queryset
    # }
    # return HttpResponse(context)
    # return render(request, 'posts/home.html', context)

    # return render(request, 'posts/home.html', context)
    # return HttpResponse('Django na prática - Hello tasks!')

    # instance = get_object_or_404(Task, id=name)

    # tasks = Task.objects.all()
    return HttpResponse(instance)
    # return render(request, "tasks/task_list.html", { "tasks": tasks,})


# Retrieve a single task
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", { "task": task, })


# Update a single task
def task_update(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk,]))
    else:
        form = TaskForm(instance=task_obj)

    return render(request, "tasks/task_form.html", { "form": form, "object": task_obj})


# Delete a single task
def task_delete(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()
    return redirect(reverse("tasks:task_list"))