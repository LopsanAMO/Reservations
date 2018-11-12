from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Reservations.apps.hotels.models import Hotel, Room
from Reservations.apps.quotations.models import Reservations
from Reservations.apps.users.permissions import IsUserOrReadOnly
from Reservations.apps.quotations.api.v1.serializers import ReservationSerializer, CreateReservationSerializer


class CreateReservationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Reservations.objects.all()
    serializer_class = CreateReservationSerializer
    permission_classes = (IsUserOrReadOnly,)


class ReservationViewSet(mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsUserOrReadOnly, )
    lookup_field = 'id'
    lookup_value_regex = '[0-9]'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        reservs = Reservations.objects.filter(user=request.user)
        return Response(ReservationSerializer(reservs, many=True).data)

    def put(self, request, *args, **kwargs):
        #import pudb;pudb.set_trace()
        instance = Reservations.objects.get(id=kwargs['id'])
        reservations = Reservations.objects.filter(
            room=instance.room,
            start_date__gte=request.data['start_date'],
            end_date__lte=request.data['start_date']
        ).exclude(pk=instance.id)
        if len(reservations) >= 1:
            return Response(data={'detail': 'This room is not available'}, status=400)
        serializer = ReservationSerializer(instance, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'detail': 'Ok'}, status=200)

