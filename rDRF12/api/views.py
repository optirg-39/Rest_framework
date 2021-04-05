from django.shortcuts import render
from rest_framework.response import Response
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class StudentsAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu_data = Students.objects.get(id=id)
            python_native_data = StudentModelSerializer(stu_data)
            return Response(python_native_data.data)

        stu_all = Students.objects.all()
        python_naitve_data_all = StudentModelSerializer(stu_all, many=True)
        return Response(python_naitve_data_all.data)


    def post(self,request,format=None):
        de_serializer_data = StudentModelSerializer(data=request.data)
        if de_serializer_data.is_valid():
            de_serializer_data.save()
            return Response({'msg': 'You data is created/saved'}, status=status.HTTP_201_CREATED)
        return Response(de_serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None, format=None):
        id = pk
        stu = Students.objects.get(pk=id)
        de_sez_data = StudentModelSerializer(stu, data=request.data)
        if de_sez_data.is_valid():
            de_sez_data.save()
            print(id)
            return Response({'msg': 'Your data is completeley updated'}, status=status.HTTP_100_CONTINUE)
        return Response(de_sez_data.errors, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk = None, format=None):
        id = pk
        stu = Students.objects.get(pk = id)
        de_sez_data = StudentModelSerializer(stu, data=request.data, partial=True)
        if de_sez_data.is_valid():
            de_sez_data.save()
            return Response({'msg': 'Your data is updated partialy'})
        return Response(de_sez_data.errors, status=status.HTTP_205_RESET_CONTENT)
    def delete(self ,request ,pk =None ,format=None):
        id = pk
        stu = Students.objects.get(id)
        stu.delete()
        return Response({'msg': f'Deleted id {id} data'})
