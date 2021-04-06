# Concrete View classes
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentCreate(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentListCreate(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer