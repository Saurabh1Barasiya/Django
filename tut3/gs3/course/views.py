from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python_course(request):
    return HttpResponse("Python course")

def django_course(request):
    return HttpResponse("Django course")
