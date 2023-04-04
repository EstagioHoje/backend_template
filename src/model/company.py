from django.db import models
import uuid

class Company(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False)

    fantasy_name = models.CharField(max_length=65)
    corporate_name = models.CharField(max_length=65)
    cnpj = models.CharField(primary_key=True, unique=True, max_length=100)
    line_of_business = models.CharField(max_length=65)

    representative_name = models.CharField(max_length=65)
    representative_job = models.CharField(max_length=65)
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=65)

    cep = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    complement = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        managed = False
        db_table = 'Company'