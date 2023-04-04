from rest_framework import serializers
from ..model.report import Report

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model=Report 
        fields="__all__" #("name", "course")

class IdSerializer(serializers.Serializer): 
    # This is the one used in YASG's `query_serializer`
    id = serializers.IntegerField()