from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Student
from django.views.generic.base import TemplateView
from django import forms
# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'

    def get_form(self):
        form = super().get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"placeholder": "Enter your name", "class": "form-control"})

        form.fields["email"].widget = forms.TextInput(attrs={"placeholder": "Enter your email", "class": "form-control"})

        form.fields["password"].widget = forms.PasswordInput(attrs={"placeholder": "Enter your password", "class": "form-control"})

        return form

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanksupdate/'

    def get_form(self):
        form = super().get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"placeholder": "Enter your name", "class": "form-control"})

        form.fields["email"].widget = forms.TextInput(attrs={"placeholder": "Enter your email", "class": "form-control"})

        form.fields["password"].widget = forms.PasswordInput(attrs={"placeholder": "Enter your password", "class": "form-control"})
            
        return form

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanksupdate.html'