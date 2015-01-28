from django import forms
from django.contrib.auth import authenticate

from localflavor.us.forms import USPhoneNumberField

from .global_vars import YEAR_IN_SCHOOL_CHOICES, MAJOR_CHOICES
from .models import User, Member



class RegisterForm(forms.Form):
    username = forms.RegexField(
        label = 'K-State eID',
        max_length = 30,
        regex = r'^[a-z0-9-_]+$',
        error_messages = {
            'invalid': 'Lowercase alphanumeric characters, underscores, and dashes only (a-z, 0-9, _, -)'
        },
        widget = forms.TextInput(
            attrs = {'autofocus':'autofocus', 'placeholder':'K-State eID'}
        ),
    )
    first_name = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs = {'placeholder':'John'}
        ),
    )
    last_name = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs = {'placeholder':'Doe'}
        ),
    )
    email = forms.EmailField(
        help_text = "Does not have to be your k-state email.",
        widget = forms.TextInput(
            attrs = {'placeholder':'johndoe@ksu.edu'}
        ),
    )
    password = forms.CharField(
        max_length = 30,
        widget = forms.PasswordInput(
            attrs = {'placeholder':'Password'}
        ),
        min_length = 6,
        help_text = "Please not your K-State password. 6 or more characters.",
    )
    confirm_password = forms.CharField(
        max_length = 30,
        widget = forms.PasswordInput(
            attrs = {'placeholder':'Confirm Password'}
        ),
        min_length = 6,
    )
    phone = USPhoneNumberField(
        required = False,
        help_text='10 digits, separated by hyphens: xxx-xxx-xxxx',
        widget = forms.TextInput(
            attrs = {'placeholder':'785-532-6011'}
        ),
    )
    year_in_school = forms.ChoiceField(
        choices = YEAR_IN_SCHOOL_CHOICES,
        required = False,
    )
    major = forms.ChoiceField(
        choices = MAJOR_CHOICES,
        required = False,
    )
    ksu_identification_code = forms.IntegerField(
        max_value = 999999999999999999,
        min_value = 100000000000,
        help_text = "Swipe your K-State ID Card. This is <strong>not</strong> your WID number.",
    )

    sign_in_to_active_meetings = forms.BooleanField(
        help_text = "Sign new user into meetings available for signin?",
        required = False,
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data



class SigninForm(forms.Form):
    ksu_identification_code = forms.IntegerField(
        max_value = 999999999999999999,
        min_value = 100000000000,
        help_text = "Swipe your K-State ID Card. This is <strong>not</strong> your WID number.",
        required = False,
        widget = forms.TextInput(
            attrs = {'autofocus':'autofocus'}
        ),
    )
    username = forms.RegexField(
        label = 'K-State eID',
        widget = forms.TextInput(
            attrs = {'placeholder':'K-State eID'}
        ),
        max_length = 30,
        regex = r'^[a-z0-9-_]+$',
        required = False,

    )
    password = forms.CharField(
        max_length = 30,
        widget = forms.PasswordInput(
            attrs = {'placeholder':'Attendance Password'}
        ),
        min_length = 6,
        required = False,
    )

    def clean(self):
        ksu_identification_code = self.cleaned_data.get('ksu_identification_code')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if ksu_identification_code == "" and username == "":
            raise forms.ValidationError("Either swipe ID card, or input eID and attendance password.")

        if ksu_identification_code is not None:
            try:
                member = Member.objects.get(ksu_identification_code=ksu_identification_code)
            except Member.DoesNotExist:
                raise forms.ValidationError("Invalid KSU Identification Code. Swipe again, or sign in with eID and attendance password.")

        if username != "":
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid eID and attendance password.")

        return self.cleaned_data
