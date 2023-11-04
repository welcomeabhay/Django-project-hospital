from rest_framework import serializers
from base.models import *

class Patient_serializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'