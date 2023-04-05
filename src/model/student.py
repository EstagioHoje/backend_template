from django.db import models
import uuid
# from django.core.validators import MaxValueValidator

class Student(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    cpf = models.CharField(primary_key=True, max_length=100)
    college = models.CharField(max_length=100)
    entry_year = models.DateField()
    email = models.CharField(max_length=100)
    university_id = models.CharField(max_length=65)
    class_schedule = models.JSONField(blank=True)
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    complement = models.CharField(max_length=100, blank=True, default='')
    school = models.CharField(max_length=100)
    resumee = models.CharField(max_length=1000, blank=True, default='')

    class Meta:
        managed = False
        db_table = 'Student'