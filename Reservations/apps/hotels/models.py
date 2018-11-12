from django.db import models


class Hotel(models.Model):
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()

    def __str__(self):
        return "Hotel: {}".format(self.name)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20, unique=True)
    availability = models.BooleanField(default=True)
    price = models.CharField(max_length=16)
    description = models.TextField()

    def __str__(self):
        return "Room: {}. Hotel: {}".format(self.room_number, self.hotel.name)

