from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration
# Create your views here.
def student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:   
        form = StudentRegistration()
    return render(request, 'enroll/student.html',{'form': form})

def teacher(request):
    if request.method == 'POST':
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherRegistration()
    return render(request, 'enroll/teacher.html',{'form':form})