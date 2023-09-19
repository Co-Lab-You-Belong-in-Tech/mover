from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from django.contrib.auth.base_user import BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    charging_rate = (
        ("FX", "Fixed"),
        ("HR", "Hourly"),
    )
    ROLE_CHOICES = (
        ('driver', 'Driver'),
        ('customer', 'Customer'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    username = None

    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="images/", null=True, blank=True)
    phone_number = models.CharField(
        max_length=200)  # Not nullable and not blank
    is_verified = models.BooleanField(default=False, null=True, blank=True)
    rate_of_service = models.CharField(
        max_length=100, choices=charging_rate, null=True, blank=True)
    hourly_amount = models.IntegerField(null=True, blank=True)
    fixed_amount = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    drivers_license_number = models.IntegerField(null=True, blank=True)
    license_expiration = models.DateField(null=True, blank=True)
    license_state = models.CharField(max_length=200, null=True, blank=True)
    license_zipcode = models.CharField(max_length=200, null=True, blank=True)
    drivers_license = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Vehicle(models.Model):

    license_plate = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    is_loading = models.BooleanField(default=True)
    is_unloading = models.BooleanField(default=True)
    vehicle_insurance = models.FileField(upload_to="documents/")
    vehicle_photo = models.ImageField(upload_to="images/")
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} - {self.model}"


class VehiclePhoto(models.Model):
    photo = models.ImageField(upload_to="images")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Booking(models.Model):

    ITEM_CHOICES = (
        ('1-2', '1 - 2 items'),
        ('3-5', '3 - 5 items'),
        ('6-10', '6 - 10 items'),
        ('11-15', '11 - 15 items'),
    )
    RATE_TYPE = (
        ("FX", "Fixed"),
        ("HR", "Hourly"),
    )
    SERVICE_TYPE = (
        ("LOAD", "Load"),
        ("UNLOAD", "UnLoad"),
        ("BOTH", "Both"),
    )
    VEHICLE_TYPE_CHOICES = (
        ('Truck', 'Truck'),
        ('Cargo Van', 'Cargo Van'),
        ('Moving Van', 'Moving Van'),
        ('Flatbed Truck', 'Flatbed Truck'),
        ('Box Truck', 'Box Truck'),
        ('Mini Van', 'Mini Van'),
        ('Pick Up Truck', 'Pick Up Truck'),
    )
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="driver_bookings", null=True,)
    pickup_location = models.CharField(max_length=300)
    dropoff_location = models.CharField(max_length=300)

    # is_fufuilled = models.BooleanField(default=False)
    selected_item = models.CharField(
        max_length=5,
        choices=ITEM_CHOICES,
        default='1-2',
        null=True,
    )
    vehicle_type = models.CharField(
        max_length=50,
        choices=VEHICLE_TYPE_CHOICES,
        default="Truck"
    )
    service_type = models.CharField(
        max_length=100, choices=SERVICE_TYPE, null=True, default="LOAD")
    rate_type = models.CharField(
        max_length=100, choices=RATE_TYPE, null=True, default="FX")
    photo = models.ImageField(upload_to="images", null=True)
    note = models.CharField(max_length=400, null=True)


class Goods(models.Model):
    # Best to use a form set for this.
    name = models.CharField(max_length=200)
    weight = models.IntegerField(help_text="Weight in KG")
    owner = models.ForeignKey(CustomUser, null=True,
                              blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
