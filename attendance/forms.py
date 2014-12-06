from django import forms
from django.contrib.auth.models import User



class RegisterForm(forms.Form):
    username = forms.RegexField(
        label='Username',
        max_length=30,
        regex=r'^[a-z0-9-_]+$',
        error_messages={'required': 'Please enter your name', 'invalid': 'Lowercase alphanumeric characters and underscores and dashes only (a-z, 0-9, _, -)'},
    )
    password = forms.CharField(
        label='Password',
        max_length=30,
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        max_length=30,
        widget=forms.PasswordInput,
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
