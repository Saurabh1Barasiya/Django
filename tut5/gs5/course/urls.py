from django.urls import path,include
from . import views
urlpatterns = [
    
    path('python_course/',views.python_course,name='python_course'),
]