import datetime
from rest_framework import serializers
from Reservations.apps.hotels.models import Room
from Reservations.apps.quotations.models import Reservations
from Reservations.apps.hotels.api.v1.serializers import RoomSerializer


class CreateReservationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        room = validated_data['room']
        reservations = Reservations.objects.filter(
            room=room,
            start_date__lte=validated_data['start_date'],
            end_date__gte=validated_data['start_date']
        )
        if room.availability is False and len(reservations) >= 1:
            raise serializers.ValidationError('This room is not available')
        reserv = Reservations.objects.create(**validated_data)
        room.availability = False
        room.save()
        return reserv

    class Meta:
        model = Reservations
        fields = ('id','room', 'user', 'start_date', 'end_date')
        read_only_fields = ('id',)
        extra_kwargs = {
            'room': {'write_only': True},
            'user': {'write_only': True},
            'start_date': {'write_only': True},
            'end_date': {'write_only': True},
        }


class ReservationSerializer(serializers.ModelSerializer):
    room = serializers.SerializerMethodField()

    class Meta:
        model = Reservations
        fields = ('id', 'room', 'user', 'start_date', 'end_date', 'status')
        read_only_fields = ('id', 'status', 'room', 'user')

    def get_room(self, obj):
        return RoomSerializer(obj.room).data
