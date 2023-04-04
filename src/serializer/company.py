from rest_framework import serializers
from ..model.company import Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model=Company 
        fields="__all__"


class CNPJSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cnpj = serializers.CharField(max_length=100)