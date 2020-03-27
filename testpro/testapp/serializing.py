from rest_framework import serializers
from.models import EmployeDetails
class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeDetails
        fields="__all__"
