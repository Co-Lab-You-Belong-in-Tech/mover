from django.contrib import admin
from .models import CustomUser, Vehicle, Booking


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'role', 'phone_number', 'is_verified')
    list_filter = ('role', 'is_verified')
    search_fields = ('email', 'first_name', 'last_name')
    # Add more customization options as needed


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'year', 'make',
                    'model', 'driver', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('license_plate', 'driver__email')
    # Add more customization options as needed


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('owner', 'pickup_location',
                    'dropoff_location', 'service_type', 'rate_type')
    list_filter = ('service_type', 'rate_type')
    search_fields = ('owner__email', 'pickup_location', 'dropoff_location')
    # Add more customization options as needed
