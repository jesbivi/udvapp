from django.urls import path
from user import views

urlpatterns=[
    path("user/home",views.UserHome.as_view(),name="userhome"),
    path("accounts/user/signin",views.UserRegistration.as_view(),name="userreg"),
    path("devices/all",views.ViewAllDevices.as_view(),name="alldevices"),
    path("vehicles/all",views.ViewAllVehicles.as_view(),name="allvehicles")
    ]