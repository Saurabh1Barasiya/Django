from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'course/home.html',{'name':'Saurabh'})

def about(request):
    return render(request, 'course/about.html',{'name':'Saurabh'})

def contact(request):
    return render(request, 'course/contact.html',{'name':'Saurabh'})