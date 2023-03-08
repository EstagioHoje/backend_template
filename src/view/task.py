from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser

from ..model.task import Task

from ..serializer.task import TaskSerializer

# Create your views here.

# Create a task
# @csrf_exempt
def task_create(request: HttpRequest):
    # print(f"request = {request}")
    # print(request.POST)
    # return HttpResponse(request.POST)
    task_data = JSONParser().parse(request)

    # print(task_data)
    task_serializer=TaskSerializer(data=task_data)
    if task_serializer.is_valid():
        task_serializer.save()
        return JsonResponse("Added Successfully \n\r"+str(task_data),safe=False)
    return JsonResponse("Failed to Add \n\r"+str(task_data),safe=False)
    # form.save()
    # # return HttpResponse(str(request.POST))
    # if request.method == "POST":
    #     print(f"request.POST = {request.POST}")
    #     print(f"request.query_params = {request.query_params}")
    #     form = TaskForm(request.POST)
    #     print(f"form = {form}")
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse(":task_list"))
    #     else:
    #         print(f"form.errors = {form.errors}")
    # else:
    #     form = TaskForm()

    return HttpResponse(str(form))
    # return render(request, "tasks/task_form.html", { "form": form, })


# Retrieve task list
def task_list(request: HttpRequest):
    task = Task.objects.all()
    
    task_serializer=TaskSerializer(task,many=True)
    return JsonResponse(task_serializer.data,safe=False)
    # context = json.dumps(queryset, default=str)

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
    return HttpResponse(context)
    # return render(request, "tasks/task_list.html", { "tasks": tasks,})


# Retrieve a single task
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", { "task": task, })


# Update a single task
def task_update(request, pk):
    # task_obj = get_object_or_404(Task, pk=pk)
    # if request.method == 'POST':
    #     form = TaskForm(instance=task_obj, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse("tasks:task_detail", args=[pk,]))
    # else:
    #     form = TaskForm(instance=task_obj)

    # return render(request, "tasks/task_form.html", { "form": form, "object": task_obj})
    return True


# Delete a single task
def task_delete(request, pk):
    # task_obj = get_object_or_404(Task, pk=pk)
    # task_obj.delete()
    # return redirect(reverse("tasks:task_list"))
    return True