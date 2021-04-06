# ViewSet class
from django.shortcuts import render
from rest_framework.response import Response
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework import viewsets
from rest_framework import status


class StudentsViewSet(viewsets.ViewSet):
    def List(self,request):
        stu = Students.objects.all()
        serializer_data = StudentModelSerializer(stu , many=True)
        return Response(serializer_data.data)

    def Retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Students.objects.get(id = id)
            serializer_data = StudentModelSerializer(stu)
            return Response(serializer_data.data)

    def Create(self,request):
        serialize_incomming_data = StudentModelSerializer(data= request.data)
        if serialize_incomming_data.is_valid():
            serialize_incomming_data.save()
            return Response({'msg':'Data Created'} , status=status.HTTP_201_CREATED)
        return Response({serialize_incomming_data.errors},status=status.HTTP_400_BAD_REQUEST)

    def Update(self,request,pk=None):
        stu_data_from_database = Students.objects.get(id=pk)
        serialized_data = StudentModelSerializer(stu_data_from_database, data = request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def Partil_Update(self, request, pk=None):
        stu_data_from_database = Students.objects.get(id=pk)
        serialized_data = StudentModelSerializer(stu_data_from_database, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        stu_data = Students.objects.get(id=pk)
        stu_data.delete()
        return Response({'msg':f'Data deleted for id {id}'})
























































































        pass