from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from Reservations.apps.hotels.models import Hotel, Room
from Reservations.apps.quotations.models import Reservations
from .factories import ReservationFactory
from Reservations.apps.users.test.factories import UserFactory


class TestReservationListTestCase(APITestCase):
    """
    Tests /reservations list operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        self.hotel = Hotel.objects.create(name='test', country='test', state='state', description='test')
        self.room = Room.objects.create(hotel=self.hotel, room_number='test', price='200', description='test')
        self.reservation_data = model_to_dict(ReservationFactory.build())
        self.reservation = None

    def test_post_request_with_no_data_fails(self):
        response = self.client.post('/api/v1/reservations/', {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        self.reservation_data['user'] = self.user.id
        self.reservation_data['room'] = self.room.id
        response = self.client.post('/api/v1/reservations/', self.reservation_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        self.reservation = Reservations.objects.get(pk=response.data.get('id'))
        eq_(self.reservation.room.room_number, self.room.room_number)


class TestReservationsDetailTestCase(APITestCase):
    """
    Tests /reservations detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.reservation = ReservationFactory()
        self.url = reverse('reservations-detail', kwargs={'id': self.reservation.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_list_of_reservations(self):
        response = self.client.get('/api/v1/reservations/reservation/')
        eq_(response.status_code, status.HTTP_200_OK)

    def test_get_request_returns_a_given_reservation(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

