from django import forms
from .models import User
from django.core.validators import MinLengthValidator
class StudentRegistration(forms.ModelForm):
    name = forms.CharField(validators=[MinLengthValidator(5)], max_length=10)
    # iski prority high rahti h 
    class Meta:
        model = User
        fields = '__all__'
        labels = {"name":"Enter Name", "email":"Enter Email", "password":"Enter Password"}
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Name",'id':'name'}),
            "email":forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter Email",'id':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','id':'password','placeholder':'Enter Password'}),
        }

        error_messages={
            'name':{'required':'Name is required--','min_length':'Name should be atleast 5 characters long','max_length':'Name should be atmost 10 characters long'},
            'email':{'required':'Email is required--','min_length':'Name should be atleast 5 characters long','max_length':'Name should be atmost 10 characters long'},
            'password':{'required':'Password is required--','min_length':'Name should be atleast 5 characters long','max_length':'Name should be atmost 10 characters long'},
            }
            