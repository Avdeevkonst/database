import re
from django import forms
from .models import *


class AddFile(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'


class Authorization(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
