from django.shortcuts import render
from .models import Cokiestand
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import Cokiestand_standSerializer
# Create your views here.
class ListApiView(ListCreateAPIView):
    
    queryset= Cokiestand.objects.all()
    serializer_class = Cokiestand_standSerializer

class DetailApiView(RetrieveUpdateDestroyAPIView):
    queryset= Cokiestand.objects.all()
    serializer_class = Cokiestand_standSerializer
