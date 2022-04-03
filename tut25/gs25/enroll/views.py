from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # return HttpResponseRedirect('/thankyou/')
            return HttpResponseRedirect('/enroll/thankyou/')
    else:
        fm = StudentRegistration()
    return render(request,'enroll/home.html',{'form':fm})

def thankyou(request):
    return render(request,'enroll/thankyou.html')