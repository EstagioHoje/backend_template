from django.db import models
import uuid
# from django.core.validators import MaxValueValidator

class Contract(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # student_data.name
    # student_data.full_name
    # student_data.university_id
    # student_data.course
    # student_data.rg
    # student_data.cpf
    # student_data.telephone
    # student_data.email
    # student_data.address
    # student_data.number
    # student_data.city
    # student_data.state
    # student_data.cep
    # student_data.complement
    # student_data.class_hours

    # company_data.name
    # company_data.cnpj
    # company_data.address
    # company_data.number
    # company_data.complement
    # company_data.city
    # company_data.state
    # company_data.cep
    # company_data.field
    # company_data.telephone
    # company_data.email
    # company_data.representative
    # company_data.representative_job

    duration = models.IntegerField()
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    weekly_hours = models.IntegerField()
    salary = models.IntegerField()
    transport_bonus = models.IntegerField()
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'Contract'