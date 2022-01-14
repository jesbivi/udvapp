from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
    device_name=models.CharField(max_length=120,default=True)
    device_imei = models.PositiveIntegerField(max_length=15)
    primary_sim = models.PositiveIntegerField(max_length=10)
    secondary_sim= models.PositiveIntegerField(max_length=10)
    firmware_option = models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.device_name

class DeviceManagement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    device=models.ForeignKey(Device,on_delete=models.CASCADE)

class Users(models.Model):
    user_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    email = models.CharField(max_length=120, unique=True)
    phone = models.CharField(max_length=15, unique=True)


    def __str__(self):
        return self.user_name

class Vehicles(models.Model):
    vehicle_name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120, unique=True)


    def __str__(self):
        return self.vehicle_name