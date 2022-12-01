from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', start, name='home'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('registration', registration, name='registration'),
    path('login', login, name="login"),
    path('info', info, name='info'),
    path('feedback', feedback, name='feedback'),
    path('user/<int:user_id>/', user_account, name='user_account')
]
