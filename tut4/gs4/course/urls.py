from django.urls import path
from . import views
urlpatterns = [
    path('python/', views.python_course, name='python_course'),
    path('django/', views.django_course, name='django_course'),
]