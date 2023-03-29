from django.db import models
import uuid
# from django.core.validators import MaxValueValidator

class Student(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=65)
    course = models.CharField(max_length=100)
    cpf = models.BigIntegerField(primary_key=True, unique=True)

    college = models.CharField(max_length=100)
    entry_year = models.BigIntegerField()
    email = models.CharField(max_length=100)
    resumee = models.CharField(max_length=100)
    # university_id = 
    telephone = models.BigIntegerField()
    address = models.CharField(max_length=100)
    cep = models.BigIntegerField()
    city = models.CharField(max_length=100)
    number = models.BigIntegerField()
    state = models.CharField(max_length=100)
    complement = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Student'