from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from Reservations.apps.hotels.api.v1.views import HotelViewSet, RoomViewSet, CreateRoomViewSet, HotelRoomViewSet


router = DefaultRouter()
router.register(r'', HotelViewSet)
router.register(r'rooms', CreateRoomViewSet)
router.register(r'room/', RoomViewSet)
router.register(r'hotel/room', HotelRoomViewSet)

urlpatterns = [
    path('', include(router.urls))
]
