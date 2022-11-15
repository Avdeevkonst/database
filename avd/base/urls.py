from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', start),
    path('info/<slug:info_s>/', info),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
