from django import forms
from .models import Person
from django.forms import ModelForm


class PersonForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Person
        fields = ['username', 'email', 'phone_no', 'password', 'details']
