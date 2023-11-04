from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import *
from base.models import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name

        return token


class Patient_view(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = Patient_serializer

class Detail_view(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = Patient_serializer