from django.urls import path

from house.views import HouseAPIView, house_home, HouseAPIViewDetail, house_findAll_by_name

urlpatterns = [
    path('house', HouseAPIView.as_view()),
    path('house/<int:pk>', HouseAPIViewDetail.as_view()),
    path('house/home', house_home),
    path('house/find_all_by_name', house_findAll_by_name),
]