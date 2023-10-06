from datetime import datetime

from django.http import JsonResponse
from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from house.models import House
from house.serializers import HouseSerializer
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class HouseAPIView(APIView):

    def get(self, request):
        print(f"--> {request}")
        house_list = House.objects.all()
        print(f"--> Total: {len(house_list)}")
        serializer = HouseSerializer(house_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=400)

class HouseAPIViewDetail(APIView):
    def get(self, request, pk):
        print(f"--> {request}")
        try:
            house = House.objects.filter(pk=pk).first()
            print(f"--> {house}")
            if house:
                serializer = HouseSerializer(house)
                return JsonResponse(serializer.data, safe=False)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as all:
            print(f"--> {all}")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        house = House.objects.filter(pk=pk).first()
        serializer = HouseSerializer(house, data=request.data)
        if house and serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        house = House.objects.filter(pk=pk).first()
        if house:
            serializer = HouseSerializer(house, data=request.data)
            # house.delete()
            if serializer.is_valid():
                house.deleted_at = now()
                serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

def house_home(request):
    data = {'data': datetime.now()}
    return JsonResponse(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def house_findAll_by_name(request):
    query_params = request.GET
    logger.info (f"--> {query_params}")
    initial_letter = query_params.get("initial_letter", "")
    limit = int(query_params.get("limit", 100))
    offset = int(query_params.get("offset", 0))
    data = House.objects.filter(name__startswith=initial_letter)[offset:limit].values("id","name", "deleted_at", "person")
    #logger.info(f"--> {data}")
    serializer = HouseSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)