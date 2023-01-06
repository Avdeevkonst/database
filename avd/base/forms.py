from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class AddFileForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = File
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=30)
    email = forms.EmailField(label='Почта')
    content = forms.CharField(label='Поле ввода', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
