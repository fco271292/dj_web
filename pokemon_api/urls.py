from django.urls import path

from pokemon_api.views import pokemon_list

urlpatterns = [
    path('pokemeon_api/', pokemon_list),
]
