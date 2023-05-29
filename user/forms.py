from django import forms
from . models import Bus_booking,User
from django .forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from paypal.standard.forms import PayPalPaymentsForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bus_booking
        fields = "__all__"

class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
  