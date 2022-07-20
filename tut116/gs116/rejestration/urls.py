from django.urls import path
from rejestration import views
urlpatterns = [
    path('profile/', views.profile, name='profile'),
]