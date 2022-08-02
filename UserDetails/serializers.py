from rest_framework import  serializers
from .models import User
class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=20)
    dateOfBirth=serializers.DateField()
    gender=serializers.CharField(max_length=20)
    height=serializers.CharField(max_length=20)
    weight=serializers.CharField(max_length=20)

    #to POST method
    def create(self,validatedData):
        return User.objects.create(**validatedData)
    
    def update(self,instance,validatedData):
        instance.username=validatedData.get('username',instance.username)
        instance.password=validatedData.get('password',instance.password)
        instance.email=validatedData.get('email',instance.email)
        instance.dateOfBirth=validatedData.get('dateOfBirth',instance.dateOfBirth)
        instance.gender=validatedData.get('gender',instance.gender)
        instance.height=validatedData.get('height',instance.height)
        instance.weight=validatedData.get('weight',instance.weight)
        instance.save()
        print(instance.username)
        return instance



