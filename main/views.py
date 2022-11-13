from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Streamers
from .forms import SignUp, SignIn


def tariffs(request):
    return render(request, 'main/tariffs.html')


def personal_account(request):
    return render(request, 'main/personal_account.html')


def main_page(request):
    return render(request, 'main/main_page.html')


def donate_page(request):
    return render(request, 'main/donate_page.html')


def register(request):
    if request.method == 'POST':
        f = SignUp(request.POST)
        print(f)
        new_user = f.save(commit=True)
        new_user.save()
        return render(request, 'main/main_page.html', {'new_user': new_user})
    else:
        f = SignUp()
    return render(request, 'main/register_page.html', {'form': f})


def login(request):
    if request.method == 'POST':
        f = SignIn(request.POST)
        if f.is_valid():
            phone = f.cleaned_data.get("phone")
            password = f.cleaned_data.get("password")
            print(phone)
            user = Streamers.objects.filter(phone=phone)
            if user and user['password'] == password:
                return render(request, 'main/main_page.html')
    else:
        f = SignUp()
    return render(request, 'main/enter_page.html', {'form': f})



