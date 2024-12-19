"""s_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name="base"),
    path('login/',views.login_f,name="login"),
    path('login_hod/',views.login_hod,name="login_hod"),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminnhome/',views.adminnhome,name="adminnhome"),
    path('hod_home/',views.hod_home,name="hod_home"),
    path('home/',views.home,name="home"),
    path('logout/', views.logout, name="logout")
]
