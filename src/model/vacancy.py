from django.db import models
import uuid

class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #models.CharField(primary_key=True, unique=True, max_length=2000)
    
    name = models.CharField(max_length=100)
    remuneration = models.IntegerField()
    start_data = models.CharField(max_length=100)
    end_data = models.CharField(max_length=100)
    hours_per_week = models.IntegerField()
    Description = models.CharField(max_length=10000)
    cnpj_company = models.BigIntegerField()
    work_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Vacancy'