from django.db import models
from Reservations.apps.hotels.models import Room
from Reservations.apps.users.models import User


class Reservations(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='reserved')

    def __str__(self):
        return "Reservation: {}, room {}".format(self.user.email, self.room.room_number)
