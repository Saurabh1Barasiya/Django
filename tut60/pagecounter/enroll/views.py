from django.shortcuts import render

# Create your views here.
def home(request):
    # 👀👀👀👀👀👀
    # if count session hoga to nahi to default value dega (0).
    c = request.session.get('count', 0)
    nc = c + 1
    request.session['count'] = nc
    return render(request, 'enroll/home.html', {'count': nc})
