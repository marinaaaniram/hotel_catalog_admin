from rest_framework.routers import DefaultRouter

from hotels.views import HotelViewSet

router = DefaultRouter()
router.register('', HotelViewSet, basename='hotels'),

urlpatterns = [
]

urlpatterns += router.urls