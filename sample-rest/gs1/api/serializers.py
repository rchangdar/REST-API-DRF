from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    empcount = serializers.IntegerField()
    location = serializers.CharField(max_length=100)