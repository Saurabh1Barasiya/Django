from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView

# Create your views here.
class StudentDetailView(DetailView):
    model = Student

    # ye hame only single object  return karta h.

    # context ka name autometic student ban jata h.
    # matlab model name small letter me convert ho jata h.