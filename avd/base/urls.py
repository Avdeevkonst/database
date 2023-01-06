from django.urls import path, re_path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    re_path(r'^$', start, name='home'),
    re_path(r'^registration$', RegisterUser.as_view(), name='registration'),
    re_path(r'^login$', LoginUser.as_view(), name="login"),
    re_path(r'^info$', cache_page(60 * 5)(ContactFormView.as_view()), name='info'),
    re_path(r'^user_page$', user_page, name='user_page'),
    re_path(r'^addfile$', AddFile.as_view(), name="addfile"),
    re_path(r'^filelist$', FileListView.as_view(), name='file'),
    re_path(r'^logout$', logout_user, name="logout"),
    path('__debug__/', include('debug_toolbar.urls')),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]
