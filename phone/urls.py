from rest_framework import routers

from phone.views import PhoneViewSet

router = routers.DefaultRouter()
router.register('phone', PhoneViewSet)

urlpatterns = [

]

urlpatterns += router.urls
