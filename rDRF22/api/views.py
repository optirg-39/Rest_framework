# ModelViewSet class
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission
class StudentModelViewSet(viewsets.ModelViewSet):
        queryset = Students.objects.all()
        serializer_class = StudentModelSerializer
        authentication_classes = [SessionAuthentication]
        permission_classes = [MyPermission]























































































        pass