"""
URL configuration for employement_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from employee.views import *
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('registration/',registration,name='registration'),
    path('emp_login/',emp_login,name='emp_login'),
    path('emp_home/',emp_home,name='emp_home'),
    path('profile/',profile,name='profile'),
    path('logout/',Logout,name='logout'),
    path('admin_login/',admin_login,name='admin_login'),
    path('my_experience/', my_experience, name='my_experience'),
    path('edit_myexperience/',edit_myexperience,name='edit_myexperience'),
    path('my_skills/', my_skills, name='my_skills'),
    path('edit_myskills/',edit_myskills,name='edit_myskills'),
    path('user_signup/',user_signup,name='user_signup'),
    path('user_login/',user_login,name='user_login'),
    path('user_home/',user_home,name='user_home'),
    path('emp_change_password/',emp_change_password,name='emp_change_password'),
    path('user_change_password/',user_change_password,name='user_change_password'),
    path('user_profile/',user_profile,name='user_profile'),
    path('admin_home/',admin_home,name='admin_home'),
    path('admin_change_password/',admin_change_password,name='admin_change_password'),
    path('all_employees/',all_employees,name='all_employees'),
    path('user_employees/',user_employees,name='user_employees'),
    path('post-comment/<int:employee_id>/', views.post_comment, name='post_comment'),
]