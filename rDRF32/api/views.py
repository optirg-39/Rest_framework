# Concrete View classes
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentRetrieve(RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentUpdate(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentDestroy(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

