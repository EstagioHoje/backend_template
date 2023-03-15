from rest_framework import serializers
from ..model.student import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student 
        fields="__all__" #("name", "course")

class CPFSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cpf = serializers.IntegerField()