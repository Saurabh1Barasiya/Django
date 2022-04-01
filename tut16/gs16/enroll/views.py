from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def home(request):
    form = StudentRegistration(label_suffix='',initial={'name':'amit','email':'amit@gmail.com','password':'1234'})
    form.order_fields(['email','password','name'])
    return render(request, 'enroll/home.html',{'form':form})