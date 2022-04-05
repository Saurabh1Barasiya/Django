from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)    
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(name,email,password)
    else:
        form = StudentRegistration()
    return render(request, 'enroll/home.html',{'form':form})
