from django.urls import path, re_path
from ..view.contract  import ContractView

# namespace
# app_name = 'contract'

urlpatterns = [
    # Retrieve contract list
    path('get/all', ContractView.get_all),

    # Retrieve contract list
    path('get/all_uni', ContractView.get_all_uni),

    # Retrieve contract list
    path('get/all_cpf', ContractView.get_all_cpf),

    # Retrieve contract list
    path('get/all_cnpj', ContractView.get_all_cnpj),

    # Retrieve contract
    path('get/', ContractView.get_one),

    # Create a contract
    path('post/', ContractView.post),

    # Update a contract
    path('put/', ContractView.put),

    # Retrieve contract list
    path('put/sign_student', ContractView.sign_student),

    # Retrieve contract list
    path('put/reject_student', ContractView.reject_student),

    # Retrieve contract list
    path('put/sign_teacher', ContractView.sign_teacher),

    # Retrieve contract list
    path('put/reject_teacher', ContractView.reject_teacher),

    # Delete a contract
    path('delete/', ContractView.delete),
]