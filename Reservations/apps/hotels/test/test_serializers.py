from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import HotelFactory, RoomFactory
from Reservations.apps.hotels.models import Room
from Reservations.apps.hotels.api.v1.serializers import HotelSerializer, RoomSerializer


class TestCreateHotelSerializer(TestCase):

    def setUp(self):
        self.hotel_data = model_to_dict(HotelFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = HotelSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = HotelSerializer(data=self.hotel_data)
        ok_(serializer.is_valid())


class TestCreateRoomSerializer(TestCase):
    def setUp(self):
        self.hotel_data = model_to_dict(RoomFactory(hotel=HotelFactory()))

    def test_serializer_with_empty_data(self):
        serializer = RoomSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = RoomSerializer(Room.objects.get(id=self.hotel_data['id']), data=self.hotel_data)
        ok_(serializer.is_valid())
