from django.urls import path
from . import views
urlpatterns = [
    path('python/', views.python_fees, name='python_fees'),
    path('django/', views.django_fees, name='django_fees'),
]