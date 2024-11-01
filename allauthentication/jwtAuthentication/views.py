from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from basicAuthenticationSystem.models import MyDetails
from basicAuthenticationSystem.serializers import MyDetailsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class jwtAuthenticationView(generics.ListCreateAPIView):
    queryset = MyDetails.objects.all()
    serializer_class = MyDetailsSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]