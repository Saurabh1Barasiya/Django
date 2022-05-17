from django.shortcuts import render

# Create your views here.
# if you want to use session so first you apply migrate command.
# by default exist session exist 2 weeks.


def set_session(request):
    request.session['name'] = 'sang'
    request.session.set_expiry(10) #time in secound
    return render(request,'enroll/set_session.html')

def get_session(request):
    name = request.session['name']
    age=request.session.get_session_cookie_age()
    exp_age = request.session.get_expiry_age()
    exp_date = request.session.get_expiry_date()
    exp_browser = request.session.get_expire_at_browser_close()
    return render(request, 'enroll/get_session.html', {'name': name,'age': age,'exp_age': exp_age,'exp_date': exp_date,'exp_browser': exp_browser})

def del_sessions(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'enroll/del_sessions.html')

