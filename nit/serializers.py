from rest_framework.serializers import ModelSerializer
from nit.models import Client,Project
from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id","username","email"] 

class ProjectSerializer(ModelSerializer):
    users=UserSerializer(many=True,read_only=True)
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model=Project
        fields=["id","project_name","client","users","created_by"]

class ClientSerializer(ModelSerializer):

    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model = Client
        fields = ['client_name', 'projects', 'created_at','updated_at','created_by']  



