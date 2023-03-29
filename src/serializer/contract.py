from rest_framework import serializers
from ..model.contract import Contract

class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contract 
        fields="__all__" #("name", "course")

class CPFSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cpf = serializers.IntegerField()