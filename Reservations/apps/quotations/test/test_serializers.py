from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import ReservationFactory
from Reservations.apps.quotations.api.v1.serializers import ReservationSerializer


class TestCreateHotelSerializer(TestCase):

    def setUp(self):
        self.hotel_data = model_to_dict(ReservationFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = ReservationSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ReservationSerializer(data=self.hotel_data)
        ok_(serializer.is_valid())