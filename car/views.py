from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

from car.models import Car
from car.serializers import CarSerializer


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    
    renderer_classes = [JSONRenderer, XMLRenderer, ]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
