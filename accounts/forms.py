from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=123, required=True)
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username","email","is_active")


