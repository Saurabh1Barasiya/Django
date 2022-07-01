from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.students.all()
    student_data = Student.students.get_stu_id_range(1,5)
    return render(request, 'school/home.html',{'student_data':student_data})