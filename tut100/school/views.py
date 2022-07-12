from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.
class StudentListView(ListView):
    model = Student   # ------------>  student.objects.all()
    template_name = 'school/student.html'
    context_object_name = 'students'
    ordering = ['roll']
    # context = {'students': Student.objects.all()}
    # return render(request, 'school/student.html', context)