from django import forms 
from django.core import validators
class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(4)])
    email = forms.EmailField(validators=[validators.MaxLengthValidator(10)])
    password = forms.CharField(widget=forms.PasswordInput,validators=[validators.MinLengthValidator(6)])