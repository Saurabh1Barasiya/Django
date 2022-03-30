from django.shortcuts import render

# Create your views here.
def python_course(request):
    return render(request, 'course/python_course.html')