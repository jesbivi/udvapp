from django.forms import ModelForm
from user.models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=["phone","address"]