from django.db import models
import uuid

class Teacher(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=65)
    email = models.CharField(max_length=100)
    cpf = models.CharField(primary_key=True, max_length=100)

    department = models.CharField(max_length=100,blank=True,default="")
    school = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    university_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Teacher'