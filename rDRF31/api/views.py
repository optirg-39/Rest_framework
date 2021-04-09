# ModelViewSet class
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import DhoniRateThrottel

class StudentModelViewSet(viewsets.ModelViewSet):
        queryset = Students.objects.all()
        serializer_class = StudentModelSerializer
        authentication_classes = [SessionAuthentication]
        permission_classes = [IsAuthenticatedOrReadOnly]
        # permission_classes = [IsAuthenticated]
        throttle_classes = [AnonRateThrottle, DhoniRateThrottel]























































































        pass