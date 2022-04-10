from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)    
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful !!!')
    else:
        form = StudentRegistration()
    return render(request, 'enroll/home.html', {'form': form})