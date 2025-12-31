from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator  # import validator

# Create your models here.

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Cancelled"))


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField()

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    phone = models.CharField(max_length=17)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.IntegerField(default=1)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["booking_date", "booking_time"]

    def __str__(self):
        return f"{self.name} | {self.booking_date} at {self.booking_time}  ({self.number_of_guests} Guests)"
