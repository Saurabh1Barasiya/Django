from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Enter your name')
    email = forms.EmailField(initial='Enter your email')
    password = forms.CharField(initial='Enter your password')
    password1 = forms.CharField(initial='Enter your password',widget=forms.PasswordInput,help_text='yaha initial value nahi because password field is password input')