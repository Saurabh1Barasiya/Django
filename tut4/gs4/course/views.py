from django.shortcuts import render

# Create your views here.

def python_course(request):
    return render(request,'course/python_course.html')

def django_course(request):
    return render(request,'course/django_course.html')
    