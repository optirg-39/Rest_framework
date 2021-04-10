from django.shortcuts import render
from .models import Student
from .serializer import StudentSerialier
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialier
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city','name']
    # filterset_fields = ['city']
