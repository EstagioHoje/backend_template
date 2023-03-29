from django.urls import path, re_path
from ..view.teacher  import TeacherView

# namespace
# app_name = 'teacher'

urlpatterns = [
    # Retrieve teacher list
    path('get/all', TeacherView.get_all),

    # Retrieve teacher
    path('get/', TeacherView.get_one),

    # Create a teacher
    path('post/', TeacherView.post),

    # Update a teacher
    path('put/', TeacherView.put),

    # Delete a teacher
    path('delete/', TeacherView.delete),
]