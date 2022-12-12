from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', start, name='home'),
    path('registration', registration, name='registration'),
    path('login', login, name="login"),
    path('info', info, name='info'),
    path('user', user, name='user'),
    path('addfile', addfile, name="addfile")
]
