from rest_framework import routers

from car.views import CarViewSet

router = routers.DefaultRouter()
router.register("car",CarViewSet, basename="car")

urlpatterns = router.urls