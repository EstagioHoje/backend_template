from django.db import models
import uuid
# from django.core.validators import MaxValueValidator

class Student(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=65)
    course = models.CharField(max_length=100)
    cpf = models.BigIntegerField(primary_key=True, unique=True)

    class Meta:
        managed = False
        db_table = 'Student'