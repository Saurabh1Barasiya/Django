from django.shortcuts import render

# Create your views here.
# if you want to use session so first you apply migrate command.
# by default exist session exist 2 weeks.


def set_session(request):
    request.session['username'] = 'Saurabh'
    return render(request, 'enroll/set_session.html')

def get_session(request):
    # username = request.session['username']  
    # return render(request, 'enroll/get_session.html', {'username': username})

    username = request.session.get('username', 'Guest')
    return render(request, 'enroll/get_session.html', {'username': username})

def del_sessions(request):
    if 'username' in request.session:
        del request.session['username']
    return render(request, 'enroll/del_sessions.html')

