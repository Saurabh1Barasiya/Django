from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(disabled = True,widget=forms.TextInput(attrs={'class':'form-control myclass','id':'myid'}), required=False,)
    # here no need to specify max_length