from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from person.views import PersonViewSet

router = DefaultRouter()
router.register("person", PersonViewSet, basename="person")

urlpatterns = router.urls
