from django.shortcuts import render,HttpResponse
# You have to update setting.py file first then write other things.

def set_session(request):
    request.session['name'] = 'sang'
    
    # request.session.set_expiry(10) #time in secound
    return render(request,'enroll/set_session.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True # whenever you refresh page session is updated otherwise session is expired.


    # age=request.session.get_session_cookie_age()
    # exp_age = request.session.get_expiry_age()
    # exp_date = request.session.get_expiry_date()
    # exp_browser = request.session.get_expire_at_browser_close()
    # return render(request, 'enroll/get_session.html', {'name': name,'age': age,'exp_age': exp_age,'exp_date': exp_date,'exp_browser': exp_browser})
        return render(request, 'enroll/get_session.html', {'name': name})
    else:
        return HttpResponse("Session expired !!!")

def del_sessions(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'enroll/del_sessions.html')

