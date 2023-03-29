from rest_framework import serializers
from ..model.report import Report

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model=Report 
        fields="__all__" #("name", "course")

class CPFSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cpf = serializers.IntegerField()