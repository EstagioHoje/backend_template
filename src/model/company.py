from django.db import models

class Company(models.Model):
    cnpj = models.BigIntegerField( primary_key=True, unique=True)

    corporate_name = models.CharField(max_length=65)
    line_of_business = models.CharField(max_length=65)

    rh_person_name = models.CharField(max_length=65)
    rh_position_in_company = models.CharField(max_length=65)
    rh_email = models.CharField(max_length=65)
    rh_telephone = models.BigIntegerField()

    address_cep = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    address_number = models.IntegerField()
    address_city = models.CharField(max_length=65)
    address_state = models.CharField(max_length=65)
    address_complement = models.CharField(max_length=65)


    class Meta:
        managed = False
        db_table = 'Company'