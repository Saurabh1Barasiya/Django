from django.shortcuts import render

# Create your views here.
# if you want to use session so first you apply migrate command.
# by default exist session exist 2 weeks.


def set_session(request):
    request.session['username'] = '100'
    request.session['firstname'] = 'Saurabh'
    request.session['lastname'] = 'Barasiya'
    request.session.setdefault('age', '20')
    return render(request, 'enroll/set_session.html')

def get_session(request):
    keys = request.session.keys()
    values = request.session.values()
    items = request.session.items()
    return render(request, 'enroll/get_session.html', {'keys': keys, 'values': values, 'items': items})

def del_sessions(request):
    request.session.flush()
    return render(request, 'enroll/del_sessions.html')

