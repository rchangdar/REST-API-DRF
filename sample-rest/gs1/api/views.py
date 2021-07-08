from rest_framework.serializers import Serializer
from django.shortcuts import render
from .models import Student
from .models import Company
from .serializers import StudentSerializer
from .serializers import CompanySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

#  Here to create the specific object-- MODEL INSTANCE
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer_obj = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer_obj.data)
    return HttpResponse(json_data, content_type='application/json')


def company_detail(request, pk):
    com = Company.objects.get(id=pk) # convert the model instance object as per the id
    serializer_obj = CompanySerializer(com) # create serializer that converts the model instance to JSON
    json_data = JSONRenderer().render(serializer_obj.data) 
    return HttpResponse(json_data,content_type='application/json')

# Here to create the List of objects -not specific one---QUERY SET

def student_details(request):
    stu = Student.objects.all()
    ser_obj = StudentSerializer(stu, many = True)
    json_data = JSONRenderer().render(ser_obj.data)
    return HttpResponse(json_data)

def company_details(request):
    comp = Company.objects.all()
    ser_obj = CompanySerializer(comp, many= True)
    json_data = JSONRenderer().render(ser_obj.data)
    return HttpResponse(json_data)