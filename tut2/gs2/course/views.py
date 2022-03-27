from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def python_courses(request):
    return HttpResponse('<h1>Python courses</h1>')

def django_courses(request):
    return HttpResponse('<h1>Django courses</h1>')