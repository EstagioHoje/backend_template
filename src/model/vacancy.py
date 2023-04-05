from django.db import models
import uuid

class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    weekly_hours = models.IntegerField()
    address = models.CharField(max_length=100)
    physicality = models.CharField(max_length=100)
    vacancies = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    requirements = models.CharField(max_length=100)
    company_grade = models.IntegerField(blank=True,default=0)
    company_cnpj = models.CharField(max_length=100)
    candidates = models.JSONField(default=dict(cpfs=[]),blank=True)

    def number_of_candidates(self):
        return len(self.candidates['cpfs'])

    class Meta:
        managed = False
        db_table = 'Vacancy'