from django import forms
from .models import Booking
from datetime import date


class BookingForm(forms.ModelForm):
    """
    Form for creating and editing table bookings.
    Includes validation for past dates and double bookings.
    """
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'booking_date',
                  'booking_time', 'number_of_guests']

        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date',
                # AC2: Set minimum date to today to prevent past date selection in the browser
                'min': date.today().isoformat(),
            }),
            'booking_time': forms.TimeInput(attrs={
                'type': 'time',
            }),
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
        AC4: Prevents double bookings by checking if a reservation 
        already exists for the same date and time.
        """
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        # Check if both fields are filled before querying the database
        if booking_date and booking_time:
            # Query the database for existing bookings with the same date and time
            exists = Booking.objects.filter(
                booking_date=booking_date,
                booking_time=booking_time
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "This time slot is already booked. Please choose another time or date."
                )

        return cleaned_data
