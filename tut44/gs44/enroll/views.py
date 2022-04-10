
from django.shortcuts import render  
from django.contrib import messages  
from .forms import CustomUserCreationForm 
# Create your views here.

def register(request):  
    if request.POST == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully')
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'enroll/register.html', context)