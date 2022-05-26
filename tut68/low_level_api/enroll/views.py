from importlib.metadata import version
from django.shortcuts import render

from django.core.cache import cache


# Create your views here.
# 👀👀👀👀👀👀👀👀👀
# here we work on low level api
# jab hame kisi pytohn object ko cache karna hota tab ham iska use karte h.
# jab koi cheej bhut speed se change ho rahi h tab ham caching nahi karte .
# insted jab hame pata ho ki ye nahi badlegi ya bhut time ke baad badlegi tab ham caching karte h.

# 👀👀👀👀👀👀👀
# first method...

# def home(request):
#     # firstly ye dekega ki movie (key) h if h to value dega nahi to hash_expired 
#     # return kar dega
#     mv = cache.get("movie","has_expired")
#     if mv == "has_expired":
#         # matlab movie exist nahi karta.
#         #         key , value ,time in ecounds
#         cache.set("movie","The one",30)
#         # change ham yaha se karege not html

#         mv = cache.get("movie")
#     return render(request, 'enroll/home.html',{'fm':mv})



# 👀👀👀👀👀👀👀👀👀👀👀
# second method...

# def home(request):
#     # ye check get karta or if key nahi h to set kar deta h.
#     mv=cache.get_or_set('fees',600,30,version=2)
#     return render(request, 'enroll/home.html',{'fm':mv})


# def home(request):
#     data = {'name':'sonam', 'roll':101}  # change isme karna h .
#     cache.set_many(data,30)
#     mv = cache.get_many(data)
#     return render(request, 'enroll/home.html',{'stu':mv})



# def home(request):
#     cache.delete('roll')
#     return render(request, 'enroll/home.html')


# def home(request):
#     # cache.set('roll',100,600)
#     # dv = cache.decr('roll',delta=1)  # decriment.
#     dv = cache.incr('roll',delta=1)  # decriment.

#     print(dv)
#     return render(request, 'enroll/home.html')


def home(request):
    cache.clear()
    # sab clear ho jayega.
    return render(request, 'enroll/home.html')