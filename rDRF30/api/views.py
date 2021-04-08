# ModelViewSet class
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
        queryset = Students.objects.all()
        serializer_class = StudentModelSerializer
        authentication_classes = [JWTAuthentication]
        # permission_classes = [IsAuthenticatedOrReadOnly]
        permission_classes = [IsAuthenticated]























































































        pass