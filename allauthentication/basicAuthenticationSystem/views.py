from django.shortcuts import render
from rest_framework import generics
from .models import MyDetails
from .serializers import MyDetailsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication
# Create your views here.

class MydetailsList(generics.ListCreateAPIView):
    queryset = MyDetails.objects.all()
    serializer_class = MyDetailsSerializers
    authentication_classes =[BaseAuthentication]
    permission_classes = [IsAuthenticated]