from django.shortcuts import render

# Create your views here.

def home(request):
    print("I am home view")
    return render(request, 'school/home.html')

def about(request):
    return render(request, 'school/about.html')