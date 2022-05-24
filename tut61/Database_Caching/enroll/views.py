from django.shortcuts import render

# Create your views here.


# 👀👀👀👀👀👀👀👀
# Full website cache using Database.
# ham yaha puri website ko cache karege.


def home(request):
    return render(request, 'enroll/home.html')