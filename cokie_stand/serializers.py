from rest_framework import serializers
from .models import Cokiestand

class Cokiestand_standSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cokiestand
        fields = "__all__"

