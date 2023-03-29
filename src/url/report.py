from django.urls import path, re_path
from ..view.report  import ReportView

# namespace
# app_name = 'report'

urlpatterns = [
    # Retrieve report list
    path('get/all', ReportView.get_all),

    # Retrieve report
    path('get/', ReportView.get_one),

    # Create a report
    path('post/', ReportView.post),

    # Update a report
    path('put/', ReportView.put),

    # Delete a report
    path('delete/', ReportView.delete),
]