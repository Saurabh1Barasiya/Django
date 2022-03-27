from django.urls import path
from . import views

urlpatterns = [
    path('python_course/', views.python_course),
    path('django_course/', views.django_course),
]