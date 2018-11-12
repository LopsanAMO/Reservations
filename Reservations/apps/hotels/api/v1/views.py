from rest_framework import viewsets, mixins
from rest_framework.response import Response
from Reservations.apps.hotels.models import Hotel, Room
from Reservations.apps.users.permissions import IsUserOrReadOnly
from Reservations.apps.hotels.api.v1.serializers import HotelSerializer, RoomSerializer, HotelRoomSerializer


class HotelViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (IsUserOrReadOnly,)
    lookup_field = 'id'
    lookup_value_regex = '[0-9]'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def list(self, request):
        queryset = Hotel.objects.all()
        serializer = HotelSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class CreateRoomViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsUserOrReadOnly,)


class RoomViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsUserOrReadOnly,)
    lookup_field = 'id'
    lookup_value_regex = '[0-9]'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class HotelRoomViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelRoomSerializer
    permission_classes = (IsUserOrReadOnly,)
    lookup_field = 'id'
    lookup_value_regex = '[0-9]'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

