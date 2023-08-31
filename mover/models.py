from django.db import models

# Create your models here.

# class Vehicle(models.Model):
#     name = models.CharField(max_length=30)
#     model = models.IntegerField()
#     carphoto = models.ImageField()
#     isAvailable = models.BooleanField(default=True)
#     isLoading = models.BooleanField(default=True)
#     vehicle_insurance = models.FileField()

# class DriverSignUp(models.Model):
#     id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     isVerified = models.BooleanField(default=False)
#     password = models.CharField(max_length=30)
#     rateOfService = models.TextField()
#     hourlyAmount =  models.IntegerField()
#     fixedAmount = models.IntegerField()
#     rating = models.IntegerField()
#     location = models.TextField()
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     drivers_license = models.FileField()
    
# class CustomerSignup(models.Model):
#     pass


    
# class Booking(models.Model):
#     driver = models.ForeignKey(DriverSignUp, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     pickup_location = models.TextField()
#     goods_names = models.CharField(max_length=225)
#     goods_weight = models.IntegerField()