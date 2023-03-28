from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# signup


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='username *', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}), required=True)
    password1 = forms.CharField(
        label='password *', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(label='Confirm password *', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    email = forms.CharField(label='Email *', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# login


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
                                                    attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
