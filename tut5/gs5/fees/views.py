from django.shortcuts import render

# Create your views here.
def python_fees(request):
    return render(request,'fees/python_fees.html')