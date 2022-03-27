from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def python_fees(request):
    return HttpResponse("Python feee --> 5000")

def django_fees(request):
    return HttpResponse("Django feee --> 10000")
