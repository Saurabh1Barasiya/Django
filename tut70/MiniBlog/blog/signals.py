from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(user_logged_in,sender=User)
def login_sucess(sender,request,user,**kwargs):
    print("User logged in successfully")
    print("Logged in ..... Run Intro")
    print("Sender : ",sender)
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    print("IP : ",ip)
    # print("kwargs :",kwargs)