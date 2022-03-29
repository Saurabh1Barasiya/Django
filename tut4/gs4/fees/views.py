from django.shortcuts import render

# Create your views here.
def python_fees(request):
    course_fees = {"react": "15000", "django": "20000", "flask": "25000"}
    return render(request,'fees/python_fees.html',context=course_fees)

def django_fees(request):
    return render(request,'fees/django_fees.html',{"react": "15000", "django": "20000", "flask": "25000"})