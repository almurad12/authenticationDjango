from rest_framework import serializers
from .models import MyDetails

class MyDetailsSerializers(serializers.Serializer):
    class Meta:
        models = MyDetails