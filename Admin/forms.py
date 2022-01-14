from django import forms
from django.forms import ModelForm
from Admin.models import Device,Vehicles,Users,DeviceManagement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DeviceForm(ModelForm):
    class Meta:
        model=Device
        fields="__all__"
        widgets={
            "device_name":forms.TextInput(attrs={"class":"form-control"}),
            "device_imei":forms.TextInput(attrs={"class":"form-control"}),
            "primary_sim":forms.TextInput(attrs={"class":"form-control"}),
            "secondary_sim":forms.TextInput(attrs={"class":"form-control"}),
            "firmware_option":forms.TextInput(attrs={"class":"form-control"})
        }

class UserForm(ModelForm):
    class Meta:
        model=Users
        fields="__all__"
        widgets={
            "user_name":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),

        }

class VehicleForm(ModelForm):
    class Meta:
        model=Vehicles
        fields="__all__"
        widgets={
            "vehicle_name":forms.TextInput(attrs={"class":"form-control"}),
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),

        }

class DeviceManagmentForm(ModelForm):
    class Meta:
        model=DeviceManagement
        fields = "__all__"
        widgets = {
            "device_name": forms.TextInput(attrs={"class": "form-control"}),
            "user_name": forms.TextInput(attrs={"class": "form-control"}),
        }

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }

class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))