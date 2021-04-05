from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


# ''' Default @api_view(['GET']) hota hai'''
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello world India '})

# '''for POST request'''
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print('body data',request.body)
#         '''request.data contains the parsed content of request.body'''
#         print('data data',request.data)
#         return Response({'msg' : 'This is post request'})

'''for both POST and GET'''
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg': 'Hello world', 'request': 'this is GET request'})
    elif request.method == 'POST':
        print('body data', request.body)
        '''request.data contains the parsed content of request.body'''
        print('data data',request.data)
        return Response({'msg' : 'This is post request', 'data': request.data})

