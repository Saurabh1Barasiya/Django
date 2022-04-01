from django import forms
class StudentRegistration(forms.Form):
    # here length is not required.
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())