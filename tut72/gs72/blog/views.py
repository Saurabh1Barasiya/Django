from django.shortcuts import render,HttpResponse
from blog import signals
# Create your views here.

def home(request):
    signals.notification.send(sender=None, request=request, user=["Saurabh","Barasiya"])
    return HttpResponse("Example of custom signal,jese hi home page chalega to ye signal execute hoga.")