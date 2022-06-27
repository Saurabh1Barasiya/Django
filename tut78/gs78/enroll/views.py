from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.all().order_by('-id') # it gives in the desending order.
    # student_data = Student.objects.all().order_by('id') # it gives in the asending order.
    # student_data = Student.objects.all().order_by('?') # it gives random data.
    # student_data = Student.objects.filter(city="harrai") 
    # student_data = Student.objects.filter(city="harrai").reverse()[:] 

    # student_data = Student.objects.exclude(id=5)

    # student_data = Student.objects.values_list('id','name','roll',named=True)
    # student_data = Student.objects.values_list('id','name','roll','city','marks','pass_date',named=True)

    stu = Student.objects.all()
    tea = Teacher.objects.all()

    student_data=stu.union(tea)

    print(student_data.query)   
    return render(request,'enroll/home.html',{'student_data':student_data})

