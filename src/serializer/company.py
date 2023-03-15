from rest_framework import serializers
from ..model.company import Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model=Company 
        fields="__all__"