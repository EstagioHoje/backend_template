from rest_framework import serializers
from ..model.report import Report

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model=Report 
        fields="__all__" #("name", "course")

class CPFSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cpf = serializers.CharField(max_length=100)

class IDSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    id = serializers.CharField(max_length=100)

class UNISerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    uni = serializers.CharField(max_length=100)

class CNPJSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cnpj = serializers.CharField(max_length=100)