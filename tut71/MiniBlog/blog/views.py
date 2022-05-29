from django.shortcuts import render,HttpResponseRedirect
from .models import Post
from .form import Signup_form,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.core.cache import cache


# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})

def about(request):
    return render(request, 'blog/about.html',)

def contact(request):
    return render(request, 'blog/contact.html',)

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title,desc=desc)
                post.save()
                messages.success(request, 'Post added successfully!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm()
        return render(request, 'blog/add_post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def update_post(request,id):    
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        if request.method == 'POST':
            form = PostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post updated successfully!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        name = request.user.username
        full_name = request.user.get_full_name()
        gps = request.user.groups.all()

        ip = request.session.get('ip',0.0)
        user = request.user
        ct = cache.get('count',0,version=user.pk)
        return render(request, 'blog/dashboard.html',{'posts':posts,'name':name,'full_name':full_name,'groups':gps,'ip':ip,'count':ct})
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            messages.success(request, 'Account created successfully!')  
    else:
        form = Signup_form()
    return render(request, 'blog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Login Successful!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logout Successful!!!')
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')