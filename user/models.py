from django.db import models
from django.contrib.auth.models import User
from Admin.models import Device,Vehicles

# Create your models here.
class UserProfile(models.Model):
    phone=models.CharField(max_length=12,unique=True)
    address=models.CharField(max_length=120)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class DisplayDevice(models.Model):
    book=models.ForeignKey(Device,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class DisplayVehicle(models.Model):
    book=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)