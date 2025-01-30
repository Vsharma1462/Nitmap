from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Client,Project
from nit.serializers import ClientSerializer,ProjectSerializer,UserSerializer
from django.contrib.auth.models import User


# Create your views here. 

class ClientViewCRUD(ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


class ProjectViewCRUD(ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer  

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UsersViewCRUD(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer   
