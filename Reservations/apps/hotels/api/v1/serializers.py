from rest_framework import serializers
from Reservations.apps.hotels.models import Hotel, Room


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id','country', 'state', 'name', 'description')
        read_only_fields = ('id',)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'hotel', 'room_number', 'availability', 'price', 'description')
        read_only_fields = ('availability',)
        dept = 1


class HotelRoomSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'rooms')

    def get_rooms(self, obj):
        rooms = Room.objects.filter(hotel=obj)
        return RoomSerializer(rooms, many=True).data