from django.shortcuts import render
from .models import Page
# Create your views here.
def home(request):
    student_data = Page.objects.all()
    return render(request, 'enroll/home.html',{'student_data':student_data})