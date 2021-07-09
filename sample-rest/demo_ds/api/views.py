import json
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import Serializer
from .serializers import EmployeeSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def employee_create(request):#this method to insert records for the json schema
    if request.method == 'POST':#applicable only for post method
        json_data = request.body#whatever the body take it 
        stream = io.BytesIO(json_data)#convert it to byte stream
        pydata = JSONParser().parse(stream)#parse it as json
        ser_obj = EmployeeSerializer(data = pydata)#convert the python data to serializer onject 
        if(ser_obj.is_valid()):
            ser_obj.save()#save the result to json
            res = {'msg':'record succesfully created....'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(Serializer.errors)
            return HttpResponse(json_data, content_type='application/json')