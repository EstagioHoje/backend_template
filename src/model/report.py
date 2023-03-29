from django.db import models
import uuid
# from django.core.validators import MaxValueValidator

class Report(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # name = models.CharField(max_length=65)
    # course = models.CharField(max_length=100)
    # cpf = models.BigIntegerField(primary_key=True, unique=True)
    student_name = models.CharField(max_length=100)
    student_full_name = models.CharField(max_length=100)
    student_report = models.CharField(max_length=100)
    student_cpf = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_report = models.CharField(max_length=100)

    # contract_data.start_date
    # contract_data.end_date
    
    company_cnpj = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Report'