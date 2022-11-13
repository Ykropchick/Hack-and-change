from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('tariffs/', tariffs, name="tariffs"),
    path('', main_page, name="main_page"),
    path('personal_account/', personal_account, name="personal_account"),
    path('donate_page/', donate_page, name='donate_page'),
]