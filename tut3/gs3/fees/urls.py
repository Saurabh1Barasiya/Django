from django.urls import path
from . import views

urlpatterns = [
    path('python_fees/', views.python_fees),
    path('django_fees/', views.django_fees),
]