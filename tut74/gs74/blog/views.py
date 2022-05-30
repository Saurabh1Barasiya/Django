from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("Hello I am class based middleware")
    return HttpResponse("Hello I am class based middleware")
