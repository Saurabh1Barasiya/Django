from django.shortcuts import render
from .form import StudentRegistration
# Create your views here.
def home(request):
    # form = StudentRegistration(auto_id=False)
    # form = StudentRegistration(auto_id='some_%s')
    # so is should be: some_name, some_email, some_password
    # form = StudentRegistration(auto_id='kjdbfj') # treated as true

    form = StudentRegistration(auto_id=True,initial={'name':'John','email':'jhon@gmail.com','password':'password'})
    return render(request, 'enroll/home.html',{'form':form})