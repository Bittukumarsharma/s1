from django.shortcuts import render 
from .serializers import PersonSerializer 
from rest_framework import viewsets
from .models import * 
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# Create your views here.
class PersonModelViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[AllowAny] 
    permission_classes=[IsAdminUser] 