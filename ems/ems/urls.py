"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from work import views
urlpatterns = [
    path('admin/', admin.site.urls,),
    path('login/', views.login ,name='login'),
    path('login1/', views.login1,name='login1'),
    path('regist1/', views.regist1,name='regist1'),
    path('regist/', views.regist,name='regist'),
    path('home/', views.home,name='home'),
    path('home1/', views.home1,name='home1'),
    path('add/', views.add,name='add'),
    path('addemp/', views.addemp,name='addemp'),
    path("getcaptcha/", views.getcaptcha, name="getcaptcha"),
    path('update/',views.update,name='update' ),
    path('update1',views.update1,name='update1'),
    path ('del1/',views.del1 ,name='del1'),
    path('checkname/', views.checkname, name='checkname'),
    path('checkaptcha/', views.checkcaptcha, name='checkcaptcha'),
    path('jsapp/',include('jsapp.urls') ),
    path('ajax/',include('ajax.urls')),

]
