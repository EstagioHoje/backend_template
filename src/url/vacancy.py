from django.urls import path
from ..view.vacancy  import VacancyView

urlpatterns = [
    # Retrieve vacancy list
    path('get/all', VacancyView.get_all),

    # Retrieve vacancy list
    path('get/all_cnpj/', VacancyView.get_all_cnpj),

    # Retrieve vacancy list
    path('get/candidates/', VacancyView.get_candidates),

    # Retrieve vacancy
    path('getID/', VacancyView.get_one_id),

    # Create a vacancy
    path('post/', VacancyView.post),

    # Update a vacancy
    path('put/', VacancyView.put),

    # Delete a vacancy
    path('delete/', VacancyView.delete),

    # 
    path('apply/', VacancyView.apply),
]