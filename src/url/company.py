from django.urls import path
from ..view.company  import CompanyView

urlpatterns = [
    # Retrieve company list
    path('get/all', CompanyView.get_all),

    # Retrieve company
    path('get/', CompanyView.get_one),

    # Create a company
    path('post/', CompanyView.post),

    # Update a company
    path('put/', CompanyView.put),

    # Delete a company
    path('delete/', CompanyView.delete),
]