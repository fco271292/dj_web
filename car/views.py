from django.shortcuts import render
from rest_framework import viewsets

from car.models import Car
from car.serializers import CarSerializer


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer