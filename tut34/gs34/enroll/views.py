from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            # to save the data in the database
            # reg = User(name=nm, email=em, password=pw)
            # reg.save()

            # Update data to the database wich contain id = 1
            # reg = User(id=1,name=nm, email=em, password=pw)
            # reg.save()

            # Delete dta from the database wich contain id = 2
            reg = User(id=2)
            reg.delete()
            messages.success(request, 'Data saved successfully!!!')
    else:
        form = StudentRegistration()
    return render(request, 'enroll/index.html',{'form':form})