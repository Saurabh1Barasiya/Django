from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User    # import User model
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def add(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            ag = form.cleaned_data['age']
            em = form.cleaned_data['email'] 
            pw = form.cleaned_data['password']
            # created_at = form.cleaned_data['created_at']
            reg = User(name=nm, age=ag, email=em, password=pw)
            reg.save()
            form = StudentRegistration()
            messages.success(request, 'Data saved successfully!!!')
    else:
        form = StudentRegistration()
    return render(request, 'enroll/add.html',{'form':form})

def showdata(request):
    data = User.objects.all().order_by('id')
    paginator = Paginator(data,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'enroll/showdata.html',{'page_obj':page_obj})

def delete_data(request, my_id):
    if request.method == 'POST':
        pi = User.objects.get(pk=my_id)
        pi.delete()
        return HttpResponseRedirect('/showdata/')

def update_data(request,my_id):
    pi = User.objects.get(pk=my_id)
    if request.method == 'POST':
        form = StudentRegistration(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successfully!!!')
            return HttpResponseRedirect('/showdata/')
    else:
        form = StudentRegistration(instance=pi)
    return render(request, 'enroll/update.html',{'form':form})

def delete_all_data(request):
    if request.method == 'POST':
        User.objects.all().delete()
        return HttpResponseRedirect('/showdata/')