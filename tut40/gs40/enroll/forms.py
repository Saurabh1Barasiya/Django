from django import forms
from .models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class': 'form-control'}),
            # 'created_at': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }