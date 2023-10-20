from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from phone.serializers import PhoneSerializer
from phone.models import Phone


# Create your views here.
class PhoneViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                   DestroyModelMixin):

    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
