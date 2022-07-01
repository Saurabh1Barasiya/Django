from django.shortcuts import render
from .models import Student, ProxyStudent
# Create your views here.

def home(request):
    # student_data = Student.objects.all()
    student_data = ProxyStudent.student.all()
    return render(request, 'school/home.html', {'student_data': student_data})