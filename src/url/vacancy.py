from django.urls import path
from ..view.vacancy  import VacancyView

urlpatterns = [
    # Retrieve vacancy list
    path('get/all', VacancyView.get_all),

    # Retrieve vacancy
    path('get/', VacancyView.get_one),

    # Create a vacancy
    path('post/', VacancyView.post),

    # Update a vacancy
    path('put/', VacancyView.put),

    # Delete a vacancy
    path('delete/', VacancyView.delete),

    # 
    path('apply/', VacancyView.apply),
]