import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        exclude = ['password', 'is_admin', 'is_active', 'is_superuser', 'is_staff']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['phone_number'].widget.attrs['placeholder'] = 'please enter only 10 digits'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')

        pattern = r'[6-9]\d{9}'
        is_valid = re.fullmatch(pattern, phone_number)

        if not is_valid:
            self.add_error("phone_number", "Please enter valid number")


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username or Email'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
