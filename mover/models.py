from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

charging_rate = (
    ("FX", "Fixed"),
    ("HR", "Hourly"),
)

class CustomUser(AbstractUser):

    address = models.TextField(max_length=300)

    def __str__(self):
        return self.first_name


class Driver(CustomUser):

    is_verified = models.BooleanField(default=False)
    rate_of_service = models.TextField(max_length=100, choices=charging_rate)
    hourly_amount =  models.IntegerField()
    fixed_amount = models.IntegerField()
    rating = models.IntegerField()
    drivers_license = models.FileField()
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    is_loading = models.BooleanField(default=True)
    vehicle_insurance = models.FileField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class VehiclePhoto(models.Model):
    photo = models.ImageField(upload_to="images")
    vehicle = models.ForeignKey(Vehicle, on_delete = models.CASCADE)


class Booking(models.Model):
    # name = models.CharField(max_length=300)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name = "driver_bookings")
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, related_name = "customer_bookings")
    pickup_location = models.TextField(max_length=300)
    dropoff_location = models.TextField(max_length=300)
    goods_name = models.CharField(max_length=225)
    total_weight = models.IntegerField()
    total_fee = models.IntegerField()
    is_fufuilled = models.BooleanField(default=False)


class Goods(models.Model):
    # Best to use a form set for this.
    name = models.CharField(max_length=200)
    weight = models.IntegerField(help_text="Weight in KG")
    owner = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name