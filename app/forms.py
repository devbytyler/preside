from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db import models
from app.models import Person, User
from django.forms import Textarea

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username': '',
        }
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        self.cleaned_data['user'] = user
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, the username or password is invalid. Please try again.")
        return self.cleaned_data

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name",
            "apartment",
            "status",
            "gender",
            "calling",
            "notes",
            "photo_url"
        ]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)