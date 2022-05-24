from django.shortcuts import render

# 👀👀👀👀👀👀setting.py ke ander code change hua h...


# 👀👀👀👀👀👀👀👀👀👀👀👀
#  file based session.
# session store hoga session folder ke ander and 


# Create your views here.
def set_session(request):
    request.session['name'] = 'sang'
    return render(request,'enroll/set_session.html')

def get_session(request):
    name = request.session['name']
    return render(request, 'enroll/get_session.html', {'name': name})

def del_sessions(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'enroll/del_sessions.html')

    