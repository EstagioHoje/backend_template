from rest_framework import serializers
from ..model.task import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task 
        fields="__all__" #("task_id", "name", "course")
