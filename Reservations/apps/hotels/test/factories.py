import factory
from factory.fuzzy import FuzzyInteger
from Reservations.apps.hotels.models import Hotel, Room


class HotelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hotel

    country = 'Mexico'
    state = 'Ciudad de Mexico'
    name = factory.Sequence(lambda n: f'testname{n}')
    description = factory.Sequence(lambda n: f'testdescription{n}')


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    hotel = factory.SubFactory(HotelFactory)
    room_number = factory.Faker('word')
    price = FuzzyInteger(1, 100, step=1)
    description = factory.Sequence(lambda n: f'test_description{n}')