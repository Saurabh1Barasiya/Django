from django.urls import path,include
from . import views
urlpatterns = [
    
    path('python_fees/',views.python_fees,name='python_fees'),
]