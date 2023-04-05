from rest_framework import serializers
from ..model.student import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student 
        fields="__all__" #("name", "course")

class CPFSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cpf = serializers.CharField(max_length=100)

class COMPANYSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cpf = serializers.CharField(max_length=100)
    id = serializers.CharField(max_length=100)