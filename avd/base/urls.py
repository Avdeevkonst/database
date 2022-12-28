from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'^$', start, name='home'),
    re_path(r'^registration$', RegisterUser.as_view(), name='registration'),
    re_path(r'^login$', LoginUser.as_view(), name="login"),
    re_path(r'^info$', info, name='info'),
    re_path(r'^user$', user, name='user'),
    re_path(r'^addfile$', AddFile.as_view(), name="addfile"),
    re_path(r'^filelist$', FileListView.as_view(), name='file'),
    re_path(r'^logout$', logout_user, name="logout"),
    path('__debug__/', include('debug_toolbar.urls')),
]
