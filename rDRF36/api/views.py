from django.shortcuts import render
from .models import Student
from .serializer import StudentSerialier
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialier
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    ordering_fields = ['name','city']

