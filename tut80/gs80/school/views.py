from django.shortcuts import render
from .models import Student,Exam_center
# Create your views here.

def home(request):
    student_data = Student.objects.all()
    exam_center_data = Exam_center.objects.all()
    return render(request, 'school/home.html',{'exam_center_data':exam_center_data,'student_data':student_data})