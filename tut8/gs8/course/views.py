from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'course/home.html')

def about(request):
    return render(request, 'course/about.html')

def contact(request):
    return render(request, 'course/contact.html')