from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    stu = Student.objects.all()
    return render(request, 'home.html',{'stu':stu})
