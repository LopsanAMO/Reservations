from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from Reservations.apps.hotels.models import Hotel, Room
from .factories import HotelFactory, RoomFactory
from Reservations.apps.users.test.factories import UserFactory


class TestHotelListTestCase(APITestCase):
    """
    Tests /hotel list operations.
    """

    def setUp(self):
        self.url = reverse('hotel-list')
        self.hotel_data = model_to_dict(HotelFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.hotel_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        hotel = Hotel.objects.get(pk=response.data.get('id'))
        eq_(hotel.name, self.hotel_data.get('name'))


class TestHotelDetailTestCase(APITestCase):
    """
    Tests /hotel detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.hotel = HotelFactory()
        self.url = reverse('hotel-detail', kwargs={'id': self.hotel.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_given_hotel(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)


class TestRoomListTestCase(APITestCase):
    """
    Tests /room list operations.
    """

    def setUp(self):
        self.url = reverse('room-list')
        self.hotel = Hotel.objects.create(name='test', country='test', state='state', description='test')
        self.room_data = model_to_dict(RoomFactory())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        self.room_data['room_number'] = 'dsadsa'
        self.room_data['hotel'] = self.hotel.id
        response = self.client.post(self.url, self.room_data)
        eq_(response.status_code, status.HTTP_201_CREATED)
        hotel = Room.objects.get(pk=response.data.get('id'))
        eq_(hotel.room_number, self.room_data.get('room_number'))


class TestRoomDetailTestCase(APITestCase):
    """
    Tests /hotel/room detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.hotel = Hotel.objects.create(name='test', country='test', state='state', description='test')
        self.room = Room.objects.create(hotel=self.hotel, room_number='test', price='200', description='test')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_given_hotel(self):
        response = self.client.get('/api/v1/hotels/hotel/room/{}/'.format(self.hotel.id))
        eq_(response.status_code, status.HTTP_200_OK)