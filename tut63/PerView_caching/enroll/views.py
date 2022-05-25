from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

# 👀👀👀👀👀👀👀👀👀 
# PerView Cashing using Database.

@cache_page(30)
def Home(request):
    return render(request, 'enroll/home.html')

def about(request):
    return render(request, 'enroll/about.html')

