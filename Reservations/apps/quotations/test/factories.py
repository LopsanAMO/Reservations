import factory
from Reservations.apps.quotations.models import Reservations
from Reservations.apps.users.test.factories import UserFactory
from Reservations.apps.hotels.test.factories import RoomFactory


class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservations

    room = factory.SubFactory(RoomFactory)
    user = factory.SubFactory(UserFactory)
    start_date = '2018-12-12T14:00:00+0000'
    end_date = '2018-12-12T16:00:00+0000'