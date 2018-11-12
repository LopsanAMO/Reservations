from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from Reservations.apps.hotels.api.v1.views import HotelViewSet, RoomViewSet, CreateRoomViewSet, HotelRoomViewSet


hotel_router = DefaultRouter()
room_router = DefaultRouter()
hotel_router.register(r'', HotelViewSet)
hotel_router.register(r'hotel/room', HotelRoomViewSet)
room_router.register(r'rooms', CreateRoomViewSet)
room_router.register(r'room/', RoomViewSet)


urlpatterns = [
    path('', include(hotel_router.urls)),
    path('', include(room_router.urls))
]
