from django.urls import path

from house.views import HouseAPIView, house_home, HouseAPIViewDetail

urlpatterns = [
    path('house', HouseAPIView.as_view()),
    path('house/<int:pk>', HouseAPIViewDetail.as_view()),
    path('house/home', house_home),
]