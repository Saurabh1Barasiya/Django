from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.

class Go_to_google(RedirectView):
    url = 'https://www.google.com/'
    # permanent = False
    # def get_redirect_url(self, *args, **kwargs):
    #     return super().get_redirect_url(*args, **kwargs)