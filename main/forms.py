from django import forms
from .models import *
from django.contrib.auth.views import LoginView, AuthenticationForm


class SignUp(forms.ModelForm):
    phone = forms.CharField(label="phone", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Телефон"}))
    name = forms.CharField(label="name", widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': "Имя"}))
    password = forms.CharField(label="password", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Пароль"}))

    class Meta:
        model = Streamers
        fields = ("phone", "name", "password")


class SignIn(AuthenticationForm):
    phone = forms.CharField(label="phone", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Телефон"}))
    password = forms.CharField(label="password", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Пароль"}))

    class Meta:
        model = Streamers
        fields = ("phone", "password")

