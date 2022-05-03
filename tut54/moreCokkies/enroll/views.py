from django.shortcuts import render

# Create your views here.
def set_cokkies(request):
    response = render(request, 'enroll/set_cokkies.html')
    response.set_signed_cookie('name', 'sonam', salt='nm')
    return response

def get_cokkies(request):
    name = request.get_signed_cookie('name', salt='nm')
    return render(request, 'enroll/get_cokkies.html', {'name': name})

def del_cokkies(request):
    response = render(request, 'enroll/del_cokkies.html')
    response.delete_cookie('name')
    return response