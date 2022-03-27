from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def python_fees(request):
    return HttpResponse('<h1>Python courses fees - 5000</h1>')

def django_fees(request):
    return HttpResponse('<h1>Django courses fees - 10000</h1>')

