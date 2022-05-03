from django.shortcuts import render
from datetime import datetime,timedelta,timezone

# Create your views here.
def set_cook(request):
    response = render(request, 'enroll/set_cook.html')
    # max_age = 60*60*24*365   ye secound me count hoti h.  60 sec --- > 1 min.
    # max_age means kitne der me expire ho jayega.
    # response.set_cookie('name', 'Sonam',max_age=120)
    response.set_cookie('name', 'Sonam',expires=datetime.utcnow()+timedelta(days=2))
    return response

def get_cook(request):
    name = request.COOKIES['name']
    name = request.COOKIES.get('name','Not Set')
    return render(request, 'enroll/get_cook.html',{'name':name})

def del__cook(request):
    response = render(request, 'enroll/del_cook.html')
    response.delete_cookie('name')
    return response