from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'enroll/home.html')

def show_details(request,year):
    return render(request, 'enroll/show_details.html',{'year':year})