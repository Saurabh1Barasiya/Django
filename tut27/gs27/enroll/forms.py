from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if name != "saurabh":
            raise forms.ValidationError("Name is not correct")
        if not email.startswith('saurabh'):
            raise forms.ValidationError("Email is not correct")
        if len(password) < 4:
            raise forms.ValidationError("Password is greater than 4")
