from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roll'] = 101   
        context['name'] = 'Gaurav'
        context['age'] = 21
        return context


class AboutTemplateView(TemplateView):
    template_name = 'school/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'address':'Chhindwara'}
        return context

class ContactTemplateView(TemplateView):
    template_name = 'school/contact.html'
    
class ExtraTemplateView(TemplateView):
    template_name = 'school/extra.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name':'extra'}
        print("------------------------------------------",kwargs)
        return context
    