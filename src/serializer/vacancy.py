from rest_framework import serializers
from ..model.vacancy import Vacancy

class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model=Vacancy 
        fields="__all__"