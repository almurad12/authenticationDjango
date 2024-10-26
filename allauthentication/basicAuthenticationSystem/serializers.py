from rest_framework import serializers
from .models import MyDetails

class MyDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyDetails
        fields = '__all__'