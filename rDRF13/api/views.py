# GenericAPIView and Model Mixin
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class StudentList(ListModelMixin,GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrieve(RetrieveModelMixin,GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(UpdateModelMixin,GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDestroy(DestroyModelMixin,GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)