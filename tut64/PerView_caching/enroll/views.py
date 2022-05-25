from django.shortcuts import render

# Create your views here.

# 👀👀👀👀👀👀👀👀👀 
# PerView Cashing using Database.


def Home(request):
    return render(request, 'enroll/home.html')

def about(request):
    return render(request, 'enroll/about.html')

