from django.urls import path, re_path
from ..view.report  import ReportView

# namespace
# app_name = 'report'

urlpatterns = [
    # Retrieve report list
    path('get/all', ReportView.get_all),


        # Retrieve contract list
    path('get/all_uni', ReportView.get_all_uni),

        # Retrieve contract list
    path('get/all_cpf', ReportView.get_all_cpf),

        # Retrieve contract list
    path('get/all_cnpj', ReportView.get_all_cnpj),

    # Retrieve report
    path('get/', ReportView.get_one),

    # Create a report
    path('post/', ReportView.post),

    # Student add report
    path('put/student/', ReportView.put_student),

    # Company add report
    path('put/company/', ReportView.put_company),

    # Teacher evaluate a report
    path('put/teacher/', ReportView.put_teacher)
]