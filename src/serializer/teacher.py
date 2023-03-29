from rest_framework import serializers
from ..model.teacher import Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model=Teacher 
        fields="__all__" #("name", "course")

class CPFSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    cpf = serializers.IntegerField()