from django.urls import path, re_path
from ..view import task

# namespace
# app_name = 'task'

urlpatterns = [

    # Retrieve task list
    path('', task.task_list, name='task_list'),
    
    # Create a task
    path('create/', task.task_create, name='task_create'),


    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', task.task_detail, name='task_detail'),

    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', task.task_update, name='task_update'),

    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', task.task_delete, name='task_delete'),

]