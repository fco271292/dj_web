from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey

from person.models import Person
from person.serializers import PersonSerializer


# Create your views here.
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
    pagination_class = LimitOffsetPagination