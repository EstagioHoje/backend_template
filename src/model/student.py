from django.db import models

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Student(models.Model):
    name = models.CharField(max_length=65)
    course = models.CharField(max_length=100)
    cpf = models.IntegerField(primary_key=True, unique=True )

    class Meta:
        managed = False
        db_table = 'Student'