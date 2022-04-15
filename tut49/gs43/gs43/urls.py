"""gs43 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='login'),
    path('profile_page/', views.profile_page, name='profile'),
    path('User_logout/', views.User_logout, name='User_logout'),
    path('change_pass_with_old/', views.change_passs_with_the_help_of_old_pass, name='change_pass_with_old'),
    path('change_pass_without_old/', views.change_pass_without_old, name='change_pass_without_old'),
    path('userdetail/<int:id>', views.userdetail, name='userdetail'),
]
