from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>Hello, world. You're at the welcome page.</h1>")

def learn_python(request):
    return HttpResponse("Hello, world. You're at the learn_python page.")

def learn_django(request):
    return HttpResponse("Hello, world. You're at the learn_django page.")

def learn_math(request):
    return HttpResponse(10+10)

def learn_(request):
    return HttpResponse("<h1>Hello, world. You're at the learn_ page.</h1>")