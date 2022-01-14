from django.shortcuts import render,redirect
from django.http import HttpResponse
from Admin import forms
from Admin.models import Device,Vehicles,Users,DeviceManagement
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View,ListView,CreateView,TemplateView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from Admin.decorators import signin_required

# Create your views here.
@method_decorator(signin_required,name="dispatch")
class AdminHome(TemplateView):
    template_name="admin_home.html"

@method_decorator(signin_required,name="dispatch")
class AddDevice(CreateView):
    model = Device
    template_name ="add_device.html"
    form_class = forms.DeviceForm
    success_url = reverse_lazy("listalldevices")

@method_decorator(signin_required,name="dispatch")
class AddUser(CreateView):
    model = Users
    template_name ="add_user.html"
    form_class = forms.UserForm
    success_url = reverse_lazy("listallusers")

@method_decorator(signin_required,name="dispatch")
class AddVehicle(CreateView):
    model = Vehicles
    template_name ="add_vehicles.html"
    form_class = forms.VehicleForm
    success_url = reverse_lazy("listallvehicles")

@method_decorator(signin_required,name="dispatch")
class AllocateUser(CreateView):
    model = DeviceManagement
    template_name ="device_managment.html"
    form_class = forms.VehicleForm
    success_url = reverse_lazy("userhome")
    context_object_name = "allocates"

@method_decorator(signin_required,name="dispatch")
class AllDevices(ListView):
    model = Device
    template_name = "device_list.html"
    context={}
    context_object_name = "products"

@method_decorator(signin_required,name="dispatch")
class AllUsers(ListView):
    model = Users
    template_name = "user_list.html"
    context={}
    context_object_name = "users"

@method_decorator(signin_required,name="dispatch")
class AllVehicles(ListView):
    model = Vehicles
    template_name = "vehicle_list.html"
    context={}
    context_object_name = "vehicles"

class Registration(CreateView):
    model=Users
    template_name = "registration.html"
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy("signin")

class SignIn(TemplateView):
    template_name = "login.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        form=forms.SigninForm()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data["username"]
            pwd=form.cleaned_data["password"]
            user=authenticate(request,username=u_name,password=pwd)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect("adminhome")
                else:
                    return redirect("userhome")

            else:
                self.context["form"]=form
                return render(request,self.template_name,self.context)

@signin_required
def signout(request):
    logout(request)
    return redirect("signin")