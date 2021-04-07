from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework import status

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET','POST','PUT', 'PATCH','DELETE'])
@authentication_classes(BasicAuthentication)
@permission_classes(IsAuthenticated)
def studentapi(request, pk=None):
    if request.method == 'GET':
        python_data = request.data
        id = pk
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
            return Response({'msg' : 'You data is created/saved'}, status=status.HTTP_201_CREATED)
        return Response(de_serializer_data.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        python_data = request.data
        id = python_data.get('id')
        stu = Students.objects.get(id = id)
        de_sez_data = StudentModelSerializer(stu, data = python_data)
        if de_sez_data.is_valid():
            de_sez_data.save()
            return Response({'msg' : 'Your data is completeley updated'}, status=status.HTTP_100_CONTINUE)
        return Response(de_sez_data.errors,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        python_data = request.data
        stu = Students.objects.get(pk)
        de_sez_data = StudentModelSerializer(stu, data = python_data, partial=True)
        if de_sez_data.is_valid():
            de_sez_data.save()
            return Response({'msg' : 'Your data is updated partialy'})
        return Response(de_sez_data.errors)

    elif request.method == 'DELETE':
        python_data = request.data
        stu = Students.objects.get(pk)
        stu.delete()
        return Response({'msg' : f'Deleted id {id} data'})
    return Response({'msg' : 'Deletion Faild'})