from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Please enter your name'})
    email = forms.EmailField(error_messages={'required': 'Please enter your Email address'})
    password = forms.CharField(error_messages={'required': 'Please enter your password'})