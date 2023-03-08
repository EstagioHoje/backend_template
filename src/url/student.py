from django.urls import path, re_path
from ..view.student  import StudentView

# namespace
# app_name = 'student'

urlpatterns = [
    # Retrieve student list
    path('get/all', StudentView.get_all),

    # Retrieve student
    path('get/', StudentView.get_one),

    # Create a student
    path('post/', StudentView.post),

    # Update a student
    path('put/', StudentView.put),

    # Delete a student
    path('delete/', StudentView.delete),
]