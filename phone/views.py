from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['number']
    search_fields = ['number']
    ordering_fields = '__all__'

    @action(detail=False, methods=['get'], url_path='view-phone')
    def view_phone(self, request):
        return Response(status=status.HTTP_200_OK, data={'data':'PHONE'})