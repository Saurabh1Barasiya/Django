from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Accout created successfully')
    else:
        form = UserCreationForm()
    return render(request, 'enroll/home.html', {'form': form})