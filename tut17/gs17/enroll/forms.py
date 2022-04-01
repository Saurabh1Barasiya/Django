from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Saurabh Barasiya')
    email = forms.EmailField(initial='saurbh@gmail.com',help_text="Enter your email address.")