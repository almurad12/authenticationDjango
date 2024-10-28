from django.shortcuts import render
from rest_framework import generics
from basicAuthenticationSystem.models import MyDetails
from basicAuthenticationSystem.serializers import MyDetailsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

class MydetailsList(generics.ListCreateAPIView):
    queryset = MyDetails.objects.all()
    serializer_class = MyDetailsSerializers
    authentication_classes =[SessionAuthentication]
    permission_classes = [IsAuthenticated]