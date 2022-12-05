from django import forms
from .models import *


class AddFile(forms.Form):
    name_file = forms.CharField(max_length=30)
    slug = forms.SlugField(max_length=255)
    load_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class Authorization(forms.Form):
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(max_length=30, default="", verbose_name='Почта')
    paid_user = models.BooleanField(default=False, verbose_name='Платный пользователь')