from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        pi = User.objects.get(pk=2)
        form = StudentRegistration(request.POST,instance=pi)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            
            # save the data in the database.
            # reg = User(name=nm, email=em, password=pw)
            # reg.save()


            # delete specific data from the database.
            # reg = User(id=1)
            # reg.delete()

            # delete all the data from the database.
            # User.objects.all().delete()

            # update specific data in the database.
            form.save()


            messages.success(request, 'Data saved successfully!!!!')
    else:
        form = StudentRegistration()
    return render(request,'enroll/index.html',{'form':form})