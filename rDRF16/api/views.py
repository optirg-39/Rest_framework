# Concrete View classes
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudentListCreate(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer