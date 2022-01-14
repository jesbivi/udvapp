from django.urls import path
from Admin import views
urlpatterns=[
    path("",views.AdminHome.as_view(),name="adminhome"),
    path("user/add",views.AddUser.as_view(),name="adduser"),
    path("user/all",views.AllUsers.as_view(),name="listallusers"),
    path("device/add",views.AddDevice.as_view(),name="adddevice"),
    path("device/all",views.AllDevices.as_view(),name="listalldevices"),
    path("vehicle/add",views.AddVehicle.as_view(),name="addvehicle"),
    path("vehicle/all",views.AllVehicles.as_view(),name="listallvehicles"),
    path("allocate/add",views.AllocateUser.as_view(),name="allocateuser"),
    path("accounts/signup",views.Registration.as_view(),name="registration"),
    path("accounts/signin",views.SignIn.as_view(),name="signin"),
    path("accounts/signout",views.signout,name="signout")
    ]