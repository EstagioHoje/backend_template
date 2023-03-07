from .models import Task
from django import forms

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        #fields = "__all__"
        fields = [
            'task_id',
			'name',
    		'course'
		]