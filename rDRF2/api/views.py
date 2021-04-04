from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method =='POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        complex_data = StudentSerializer(data=python_data)
        print(complex_data)
        if complex_data.is_valid():
            complex_data.save()
            # Give Response to clint back
            rep_to_clint = {'msg': 'data received'}
            json_data_2 = JSONRenderer().render(rep_to_clint)
            return HttpResponse(json_data_2,content_type='application/json')
        else:
            # Give Response to clint back
            rep_to_clint = {'msg': 'data not recevied'}
            json_data_2 = JSONRenderer().render(rep_to_clint)
            return HttpResponse(json_data_2, content_type='application/json')
