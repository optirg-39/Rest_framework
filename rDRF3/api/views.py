from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def operations(request):
    if request.method == "PUT":
        json_data = request.body
        strem = io.BytesIO(json_data)
        python_data = JSONParser().parse(strem)
        id = python_data.get('id')
        stu = Students.objects.get(id=id)
        complex_data = StudentsSerializer(stu,python_data)
        if complex_data.is_valid():
            complex_data.save()
            # responce to clint
            rsp = {'msg' : f'data updated for id {id}'}
            json_data2 = JSONRenderer().render(rsp)
            return HttpResponse(json_data2, content_type='application/json')
        json_data2 = JSONRenderer().render(complex_data.errors)
        return HttpResponse(json_data2, content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        strem = io.BytesIO(json_data)
        python_data = JSONParser().parse(strem)
        id = python_data.get('id')
        stu_Delete = Students.objects.get(id = id)
        stu_Delete.delete()
        # response for clint
        rsp = {'msg' : f'You request for deleting data of id {id} is done'}
        json_data2 = JSONRenderer().render(rsp)
        return HttpResponse(json_data2,content_type='application/json')
    rsp = {'msg': f'You request for deleting data of id {id} is done'}
    json_data2 = JSONRenderer().render(rsp)
    return HttpResponse(json_data2, content_type='application/json')










