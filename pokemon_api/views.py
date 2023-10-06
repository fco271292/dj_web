import json

import requests
from django.http import JsonResponse
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(description="Lista pokemon", methods=["GET"])
def pokemon_list(self):
    url = "https://pokeapi.co/api/v2/pokemon"
    params = {'limit': 3}
    response = requests.get(url, params=params)
    response_json = response.json()
    response_status = response.status_code
    response_headers = response.headers
    data = {'results': response_json.get('results')}
    return JsonResponse(status=status.HTTP_200_OK, data=response_json)