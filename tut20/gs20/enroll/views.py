from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def home(request):
    form = StudentRegistration(initial={'name': 'Enter your full name'})
    # yaha initial value ki property jyadha rahti h.
    return render(request, 'enroll/home.html',{'form':form})

    # https://stackoverflow.com/questions/8360130/how-to-make-a-text-flash-in-html-javascript
    