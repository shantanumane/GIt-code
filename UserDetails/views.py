from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import routers, serializers
import json 
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def user_details(request,uid):
    if request.method=="GET":
        try:
            print('user ID '+str(uid))
            usr=User.objects.get(id=uid)
            print(usr)
            serializers=UserSerializer(usr)
            json_data=JSONRenderer().render(serializers.data)
            print('data returned '+str(json_data))
            
            return HttpResponse(json_data,content_type="application/json")
        except:
            errorMessage={}
            errorMessage['error']='User not Found'
            errorMessage=json.dumps(errorMessage)
            return HttpResponse(errorMessage)

def validateUser(request,uname):
    if request.method=="GET":
        try:
            usr=User.objects.get(username=uname)
            if(usr!=None):
                serializers=UserSerializer(usr)
                json_data=JSONRenderer().render(serializers.data)
                print('data returned '+str(json_data))
                return HttpResponse(json_data,content_type="application/json")
            else:
                errorMessage={}
                errorMessage['error']='Something Went Wrong!'
                errorMessage=json.dumps(errorMessage)
                return HttpResponse(errorMessage)
        except:
            errorMessage={}
            errorMessage['error']='User not Found'
            errorMessage=json.dumps(errorMessage)
            return HttpResponse(errorMessage)


@csrf_exempt
def signUp(request):
    if request.method=="POST":
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        Serializer=UserSerializer(data=pythonData)
        if(Serializer.is_valid()):
            Serializer.save()
            msg={'msg':'User Created Successfully !'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        jsonData=JSONRenderer().render(Serializer.errors)
        return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def updateUser(request):
    if request.method=='PUT':
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        print("pythonData"+str(pythonData))
        id=pythonData.get('id')
        currUser=User.objects.get(id=id)
        Serializer=UserSerializer(currUser,data=pythonData,partial=True)
        if(Serializer.is_valid()):
            Serializer.save()
            print(Serializer.data)
            msg={'msg':'User Updated Successfully !'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        jsonData=JSONRenderer().render(Serializer.errors)
        return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def deleteUser(request):
    if request.method=='DELETE':
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        print("pythonData"+str(pythonData))
        id=pythonData.get('id')
        usr=User.objects.get(id=id)
        if(usr!=None):
            usr.delete()
            msg={'msg':'User Deleted Successfully !'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        else:
            msg={'msg':'User Deletion Failed !'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

    jsonData=JSONRenderer().render(Serializer.errors)
    return HttpResponse(jsonData,content_type="application/json")



