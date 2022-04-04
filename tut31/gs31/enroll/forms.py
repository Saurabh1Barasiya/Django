from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5,error_messages={'required': 'Please enter your name','min_length': 'Name should be atleast 5 characters'})
    email = forms.EmailField(error_messages={'required': 'Please enter your Email address'})
    password = forms.CharField(error_messages={'required': 'Please enter your password'})