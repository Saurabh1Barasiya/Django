from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']    
    else:
        form = StudentRegistration()
    return render(request, 'enroll/index.html', {'form': form})