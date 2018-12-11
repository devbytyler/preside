from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db import models
from app.models import Person, User, Meeting
from django.forms import Textarea

class BaseForm(object):
    def add_form_control_class(self, fields, field_names=None):
        if not field_names:
            field_names = [field for field in fields]
        for field_name in field_names:
            current_class = fields[field_name].widget.attrs.get('class') or ''
            fields[field_name].widget.attrs['class'] = 'form-control' if not current_class else '{} form-control'.format(current_class)
    
    def __init__(self, *args, **kwargs):
        super().__init__(label_suffix='', *args, **kwargs)
        self.add_form_control_class(self.fields)


class LoginForm(forms.ModelForm, BaseForm):
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
        self.add_form_control_class(self.fields)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        self.cleaned_data['user'] = user
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, the username or password is invalid. Please try again.")
        return self.cleaned_data

class PersonForm(forms.ModelForm, BaseForm):
    
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
        self.add_form_control_class(self.fields)

        
class MeetingForm(forms.ModelForm, BaseForm):
    # date = forms.DateField(, required=True)

    class Meta:
        model = Meeting
        fields = [
            "date",
            "notes",
        ]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.add_form_control_class(self.fields)