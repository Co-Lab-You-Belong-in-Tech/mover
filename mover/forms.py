from allauth.account.forms import SignupForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomSignupForm(SignupForm):
    
    pass
    
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.generate_tracking_id()  # Call the method to generate the tracking ID
    #     if commit:
    #         user.save()
    #     return user