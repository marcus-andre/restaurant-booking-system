from django import forms
from .models import Booking
from datetime import date, time
from django.db.models import Sum

TIME_CHOICES = [
    (time(h, m).strftime('%H:%M'), time(h, m).strftime('%H:%M'))
    for h in range(16, 23)  # Das 16:00 às 22:00
    for m in (0, 30)        # Apenas :00 e :30
]


class BookingForm(forms.ModelForm):
    """
    Form for creating and editing table bookings.
    Includes validation for operating hours, capacity, and security.
    """
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'booking_date',
                  'booking_time', 'number_of_guests']

        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date',
                'min': date.today().isoformat(),
            }),
            'booking_time': forms.Select(
                choices=TIME_CHOICES,
                attrs={'class': 'form-control'}
            ),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'number_of_guests': forms.NumberInput(attrs={'min': 1, 'max': 20}),
        }

    def clean_booking_date(self):
        """
        AC2: Ensures the selected date is not in the past.
        """
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date < date.today():
            raise forms.ValidationError(
                "You cannot book a table for a past date.")
        return booking_date

    def clean(self):
        """
        AC4, AC5, AC6: Advanced validation for capacity, operating hours,
        and Sunday closure.
        """
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')
        new_guests = cleaned_data.get('number_of_guests', 0)

        if booking_date and booking_time:
            # AC6: Operating Hours Check (16:00 to 22:00)
            if booking_time < time(16, 0) or booking_time > time(22, 0):
                raise forms.ValidationError(
                    "The restaurant is open for dinner from 16:00 to 22:00."
                )

            # AC6: Sunday Closure Check (6 represents Sunday)
            if booking_date.weekday() == 6:
                raise forms.ValidationError(
                    "The restaurant is closed on Sundays. Please select another day."
                )

            # AC4 & AC5: Capacity and Double Booking Logic
            # Define the total capacity of the restaurant
            RESTAURANT_LIMIT = 20

            # Sum guests from all existing bookings for this specific slot
            existing_bookings = Booking.objects.filter(
                booking_date=booking_date,
                booking_time=booking_time
            )

            # If editing, exclude the current booking from the total sum
            if self.instance.pk:
                existing_bookings = existing_bookings.exclude(
                    pk=self.instance.pk)

            total_already_booked = existing_bookings.aggregate(
                Sum('number_of_guests')
            )['number_of_guests__sum'] or 0

            # Check if the new reservation exceeds total capacity
            if total_already_booked + new_guests > RESTAURANT_LIMIT:
                available_spots = RESTAURANT_LIMIT - total_already_booked
                raise forms.ValidationError(
                    f"Fully booked! Only {available_spots} spots left for this time."
                )

        return cleaned_data
