import datetime
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=100,error_messages={'required': 'Please enter your name'})
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False,initial=True)
    url = forms.URLField(label='Your website link', required=False,initial='http://')
    day = forms.DateField(initial=datetime.date.today)
    chose_one = forms.ChoiceField(choices=[('1','Choice 1'),('2','Choice 2'),('3','Choice 3')])
    t_time = forms.TimeField(initial='00:00')
    Resume = forms.FileField(required=False)
    
    CHOICES=[('select1','select 1'),
         ('select2','select 2')]

    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
