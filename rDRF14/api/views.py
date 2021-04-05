# GenericAPIView and Model Mixin
from .models import Students
from .serializers import StudentModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# List and Create - pk Not required
class Student_List_Create(ListModelMixin,GenericAPIView, CreateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

# Retrieve,Update and destroy -pk required
class Student_Retrieve_Destroy_Update(RetrieveModelMixin,GenericAPIView,UpdateModelMixin,DestroyModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)