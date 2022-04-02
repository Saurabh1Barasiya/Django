from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def home(request):
    form = ContactForm()
    return render(request, 'enroll/home.html',{'form':form})