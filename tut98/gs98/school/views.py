from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.

class StudentListView(ListView):
    model = Student
    # by default ye render karta h.
    # template_name = 'school/student_list.html'
    # _list.html ye by default render karta h.