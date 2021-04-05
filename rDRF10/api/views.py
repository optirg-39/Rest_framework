from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentModelSerializer

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def studentapi(request):
    if request.method == 'GET':
        python_data = request.data
        id = python_data.get('id')
        if id is not None:
            stu_data = Students.objects.get(id =id)
            python_native_data = StudentModelSerializer(stu_data)
            return Response(python_native_data.data)
        stu_all = Students.objects.all()
        python_naitve_data_all = StudentModelSerializer(stu_all,many=True)
        return Response(python_naitve_data_all.data)

    elif request.method == 'POST':
        python_data = request.data
        de_serializer_data =StudentModelSerializer(data = python_data)
        if de_serializer_data.is_valid():
            de_serializer_data.save()
            return Response({'msg' : 'You data is created/saved'})
        return Response(de_serializer_data.errors)

    elif request.method == 'PUT':
        python_data = request.data
        id = python_data.get('id')
        stu = Students.objects.get(pk = id)
        de_sez_data = StudentModelSerializer(stu, data = python_data, partial=True)
        if de_sez_data.is_valid():
            de_sez_data.save()
            return Response({'msg' : 'Your data is updated'})
        return Response(de_sez_data.errors)

    elif request.method == 'DELETE':
        python_data = request.data
        id = python_data.get('id')
        stu = Students.objects.get(pk = id)
        stu.delete()
        return Response({'msg' : f'Deleted id {id} data'})
    return Response({'msg' : 'Deletion Faild'})