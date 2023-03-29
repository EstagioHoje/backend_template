from django.db import models
import uuid
# from django.core.validators import MaxValueValidator

# class ContractData(models.Model):
#     start_date = models.CharField(max_length=100)
#     end_date = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
class Report(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    student_name = models.CharField(max_length=100)
    student_full_name = models.CharField(max_length=100)
    student_report = models.CharField(max_length=100)
    student_cpf = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_report = models.CharField(max_length=100)

    contract_data = models.JSONField() # models.ForeignKey(ContractData, on_delete=models.CASCADE)
    
    company_cnpj = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Report'