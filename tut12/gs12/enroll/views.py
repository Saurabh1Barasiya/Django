from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    stu = Student.objects.all()
    return render(request, 'enroll/index.html',{'stu':stu})
