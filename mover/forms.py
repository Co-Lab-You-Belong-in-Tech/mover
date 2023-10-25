from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser, Vehicle, Booking


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'password1',
                  'password2', 'profile_picture', 'phone_number')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', "last_name")


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class DocumentVerificationForm(UserChangeForm):

    license_expiration = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = CustomUser
        fields = ('drivers_license_number', 'license_expiration', 'license_state',
                  'license_zipcode', 'drivers_license')


class VehicleInformationForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ('license_plate', 'year', 'make', 'model',
                  'vehicle_insurance', 'vehicle_photo')


class BookingForm(forms.ModelForm):

    # selected_item = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date'})
    # )
    class Meta:
        model = Booking
        fields = ("pickup_location", "dropoff_location", "email",
                  "service_type", "rate_type",
                  )
        widgets = {
            # 'selected_item': forms.RadioSelect,
            'service_type': forms.RadioSelect,
            'rate_type': forms.RadioSelect,
            'email': forms.EmailInput()
        }


class BookingUpdateForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ("selected_item", "handle_loading", "photo", "note")
        widgets = {
            'selected_item': forms.RadioSelect,
            'handle_loading': forms.RadioSelect,
        }
