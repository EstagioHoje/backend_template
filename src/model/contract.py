from django.db import models
import uuid

# class StudentData(models.Model):
#     name = models.CharField(max_length=100)
#     full_name = models.CharField(max_length=100)
#     university_id = models.UUIDField(default=uuid.uuid4, editable=False)
#     course = models.CharField(max_length=100)
#     rg = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=100)
#     telephone = models.BigIntegerField()
#     email = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     number = models.IntegerField()
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     cep = models.IntegerField()
#     complement = models.CharField(max_length=100)
#     class_hours = models.IntegerField()    
    
#     def __str__(self):
#         return self.name
# class CompanyData(models.Model):
#     name = models.CharField(max_length=100)
#     cnpj = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     number = models.BigIntegerField()
#     complement = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     cep = models.BigIntegerField()
#     field = models.CharField(max_length=100)
#     telephone = models.BigIntegerField()
#     email = models.CharField(max_length=100)
#     representative = models.CharField(max_length=100)
#     representative_job = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Contract(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_data = models.JSONField() #models.ForeignKey(StudentData, on_delete=models.CASCADE)
    student_cpf = models.CharField(max_length=100)
    student_college = models.CharField(max_length=100)
    company_data = models.JSONField() #models.ForeignKey(CompanyData, on_delete=models.CASCADE)
    company_cnpj = models.CharField(max_length=100)

    duration = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    weekly_hours = models.IntegerField()
    salary = models.IntegerField()
    transport_bonus = models.IntegerField()
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    intership_hours = models.JSONField()
    reject_reason = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        managed = False
        db_table = 'Contract'