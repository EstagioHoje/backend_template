from django.db import models
import uuid

class Teacher(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=65)
    email = models.CharField(max_length=100)
    cpf = models.BigIntegerField(primary_key=True, unique=True)
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    # university_id = 
    full_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Teacher'