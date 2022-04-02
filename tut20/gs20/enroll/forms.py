from django import forms 
class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Enter your name',label='Name Here',label_suffix=' ',widget=forms.Textarea,help_text='Type your messages here')   # initial is a default value   