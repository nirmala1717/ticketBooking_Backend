from django.db import models
from django.contrib.auth.models import User


class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    no_of_seats = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    reach_time = models.TimeField()

    def __str__(self):
        return f"{self.bus_name} {self.number} {self.origin} {self.destination}"

class Seats(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.bus} {self.seat_number}"


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seats,on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} {self.bus.bus_name}{self.bus.start_time} {self.bus.reach_time} {self.seat.seat_number}"
    