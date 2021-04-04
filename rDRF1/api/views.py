from django.shortcuts import render
from .models import Students
from .serializers import StudentSerilazer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# model object - single Student data
def student_details(request,pk):
    stu = Students.objects.get(id=pk)
    print('waht is the name',stu)
    serializer_stu = StudentSerilazer(stu)
    print(serializer_stu)
    print(serializer_stu.data)

    # json_data = JSONRenderer().render(serializer_stu.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer_stu.data)

# model object - quary set data

def student_list(requast):
    stu2 = Students.objects.all()
    serializer_stu2 = StudentSerilazer(stu2, many=True)
    # json_data2 = JSONRenderer().render(serializer_stu2.data)
    # return HttpResponse(json_data2,content_type='application/json')
    return JsonResponse(serializer_stu2.data, safe=False)