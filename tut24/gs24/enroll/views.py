from django.shortcuts import render
from .froms import StudentRegistration
# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Data get by POST request")
            nm=fm.cleaned_data['name']
            em =fm.cleaned_data['email']
            pa =request.POST['password']
            print('name',nm,'email',em,'pass',pa)
    else:
        fm = StudentRegistration()
        print("Data get by GET request")
    return render(request, 'enroll/home.html',{'form':fm})