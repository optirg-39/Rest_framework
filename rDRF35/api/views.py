from django.shortcuts import render
from .models import Student
from .serializer import StudentSerialier
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialier
    filter_backends = [SearchFilter]
    """settings.py me default search change to rishabh"""
    # search_fields = ['city']
    search_fields = ['city','name']
    # search_fields = ['^name']
    # search_fields = ['=name']

