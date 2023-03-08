from django.db import models

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    # DepartmentId = models.AutoField(primary_key=True)
    # task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)
    course = models.CharField(max_length=100)

    class Meta:
        db_table = 'Task'
