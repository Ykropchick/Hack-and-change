from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.forms import User
from .models import Streamers
from .forms import SignUp, SignIn


def tariffs(request):
    return render(request, 'main/tariffs.html')


def personal_account(request):
    return render(request, 'main/statistic.html')


def main_page(request):
    return render(request, 'main/main_page.html')


def donate_page(request):
    return render(request, 'main/donate_page.html')


# def register(request):
#     if request.method == "Post":
#         form = SignUp(request.POST)
#         new_user = form.save(commit=False)
#
def register(request):
    if request.method == 'POST':
        f = SignUp(request.POST)
        if f.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = f.save(commit=False)
            # Set the chosen password
            # Save the User object
            new_user.save()
        return render(request, 'main/main_page.html', {'new_user': new_user})
    else:
        f = SignUp()
    return render(request, 'main/register_page.html', {'form': f})


# def login(request):
#     if request.method == 'POST':
#         f = SignIn(request.POST)
#         if f.is_valid():
#             phone = f.cleaned_data.get("phone")
#             password = f.cleaned_data.get("password")
#             user = Streamers.objects.all()
#             if user and user['password'] == password:
#                 return render(request, 'main/main_page.html')
#     else:
#         f = SignUp()
#     return render(request, 'main/enter_page.html', {'form': f})


class LoginUser(LoginView):
    form_class = SignIn
    template_name = "main/enter_page.html"

    def get_success_url(self):
        return reverse_lazy('main_page')
