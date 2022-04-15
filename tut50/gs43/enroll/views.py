from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration,MyAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User



# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = StudentRegistration(request.POST)    
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration Successful !!!')
        else:
            form = StudentRegistration()
        return render(request, 'enroll/home.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard_page/')

def user_login(request):
    if not request.user.is_authenticated:
        # if user already login h to fir vo user login page par nahi ja sakta
        if request.method == 'POST':
            form = MyAuthenticationForm(request.POST,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard_page/')
                    # here we write url name  not (name attribute)
        else:
            form = MyAuthenticationForm()
        return render(request, 'enroll/user_login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard_page/')

def dashboard_page(request):
    if request.user.is_authenticated:
        name = request.user.username
        context = {'name':name}
        return render(request, 'enroll/dashboard_page.html',context)    
    else:   
        return HttpResponseRedirect('/user_login/')

    
def User_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/user_login/')
    else:
        return HttpResponseRedirect('/user_login/')



