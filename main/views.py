from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import SignUp, SignIn


def tariffs(request):
    return render(request, 'main/tariffs.html')


def personal_account(request):
    return render(request, 'main/statistic.html')


def main_page(request):
    return render(request, 'main/main_page.html')


def donate_page(request):
    return render(request, 'main/donate_page.html')


def register(request):
    if request.method == 'POST':
        f = SignUp(request.POST)
        if f.is_valid():
            new_user = f.save(commit=False)
            new_user.save()
        return render(request, 'main/main_page.html', {'new_user': new_user})
    else:
        f = SignUp()
    return render(request, 'main/register_page.html', {'form': f})


class LoginUser(LoginView):
    form_class = SignIn
    template_name = "main/enter_page.html"

    def get_success_url(self):
        return reverse_lazy('main_page')
