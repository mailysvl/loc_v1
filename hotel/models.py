from django.db import models


class Room(models.Model):
    room_type = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    room_size = models.IntegerField()
    nightly_price = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    guests = models.IntegerField()
    breakfast_included = models.BooleanField()
    view = models.CharField(max_length=50)

    def __str__(self):
        return self.room_type
