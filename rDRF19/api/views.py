# ModelViewSet class
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework import viewsets

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = Students.objects.all()
        serializer_class = StudentModelSerializer






















































































        pass