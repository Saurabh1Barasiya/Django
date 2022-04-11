from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
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
        return HttpResponseRedirect('/profile_page/')

def user_login(request):
    if not request.user.is_authenticated:
        # if user already login h to fir vo user login page par nahi ja sakta
        if request.method == 'POST':
            form = AuthenticationForm(request.POST,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile_page/')
                    # here we write url name  not (name attribute)
        else:
            form = AuthenticationForm()
        return render(request, 'enroll/user_login.html',{'form':form})
    else:
        return HttpResponseRedirect('/profile_page/')

def profile_page(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile_page.html',{'name':request.user.username})
    else:   
        return HttpResponseRedirect('/user_login/')
    
def User_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/user_login/')
    else:
        return HttpResponseRedirect('/user_login/')

def change_passs_with_the_help_of_old_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user,data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Changed Successfully !!!')
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/profile_page/')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'enroll/change_passs_with_the_help_of_old_pass.html',{'form':form})
    else:
        return HttpResponseRedirect('/user_login/')

def change_pass_without_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user,data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Changed Successfully !!!')
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/profile_page/')
        else:
            form = SetPasswordForm(request.user)
            return render(request, 'enroll/change_pass_without_old.html',{'form':form})
    else:
        return HttpResponseRedirect('/user_login/')   # here we write url name not (name attribute)