from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'enroll/home.html')

def student(request, my_id):
    if my_id == '1':
        context ={'id':my_id}
    if my_id == '2':
        context ={'id':my_id}
    if my_id == '3':
        context ={'id':my_id}
    if my_id == '4':
        context ={'id':my_id}
    return render(request, 'enroll/student.html',context)

def student_subdata(request, my_id,my_sid):
    if my_id == 1 and my_sid == 1:
        context ={'id':my_id, 'sid':my_sid, 'name':'aman'}
    if my_id == 2 and my_sid == 2:
        context ={'id':my_id, 'sid':my_sid, 'name':'suman'}
    if my_id == 3 and my_sid == 3:
        context ={'id':my_id, 'sid':my_sid, 'name':'suman'}
    if my_id == 4 and my_sid == 4:
        context ={'id':my_id, 'sid':my_sid, 'name':'suman'}
    return render(request, 'enroll/student_subdata.html',context)