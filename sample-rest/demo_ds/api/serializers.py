from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    empid = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    zip = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)