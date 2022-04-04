from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        valname = self.cleaned_data['name']
        # if len(valname) < 3:
        #     raise forms.ValidationError('name must be at least 3 characters')
        # return valname # return the value if no error

        if valname[0] == 'S':
            raise forms.ValidationError('name cannot contain the letter first letter S')
        return valname  # return the value if no error