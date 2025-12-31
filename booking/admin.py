from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'booking_date', 'booking_time',
                    'number_of_guests', 'status')
    list_filter = ('status', 'booking_date', 'booking_time')
    search_fields = ('name', 'email')
