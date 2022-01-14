from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView
from Admin.models import Device,Vehicles
from Admin.forms import UserRegistrationForm
from user.forms import UserProfileForm


class UserHome(ListView):
    model=Device
    template_name="user_home.html"
    context_object_name ="devices"

class ViewAllDevices(ListView):
    model = Device
    template_name = "device_list.html"

class ViewAllVehicles(ListView):
    model = Vehicles
    template_name = "vehicle_list.html"

class UserRegistration(TemplateView):
    template_name = "user_reg.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user_form=UserRegistrationForm()
        profile_form=UserProfileForm()
        context["user_form"]=user_form
        context["profile_form"]=profile_form
        return context
    def post(self,request,*args,**kwargs):
        u_form=UserRegistrationForm(request.POST)
        p_form=UserProfileForm(request.POST)
        if u_form.is_valid() & p_form.is_valid():
            user=u_form.save()
            profile=p_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect("signin")
        else:
            u_form=UserRegistrationForm(request.POST)
            p_form=UserProfileForm(request.POST)
            context={}
            context["user_form"]=u_form
            context["profile_form"]=p_form
            return render(request,"user_reg.html",context)

