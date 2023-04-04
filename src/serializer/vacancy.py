from rest_framework import serializers
from ..model.vacancy import Vacancy

class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model=Vacancy 
        fields="__all__"

class ApplySerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    id_vacancy = serializers.CharField(max_length=100)
    cpf = serializers.CharField(max_length=100)