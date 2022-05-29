from ensurepip import version
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def login_sucess(sender,request,user,**kwargs):
    print("User logged in successfully")
    print("Logged in ..... Run Intro")
    print("Sender : ",sender)
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    print("IP : ",ip)
    ct = cache.get('count',0,version=user.pk)
    newcount = ct+1
    cache.set('count',newcount,60*60*24,version=user.pk)
    print(user.pk)
    # print("kwargs :",kwargs)