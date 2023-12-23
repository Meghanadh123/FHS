from django import forms
from .models import signup,ContactMessage
from .models import Reservation

class  signupForm(forms.ModelForm):
    class Meta:
        model= signup
        fields="__all__"
        widgets = {"password": forms.PasswordInput()}
        widgets = {"repeatpass": forms.PasswordInput()}


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields="__all__"
