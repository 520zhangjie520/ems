from django.urls import path
from ajax_test import views
app_name='ajaxtest'
urlpatterns=[
    path('regist/',views.regist,name='regist'),
    path('registlogic/',views.registlogic,name='registlogic'),
    path('checkname/',views.checkname,name='checkname'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('checkaptcha/',views.checkcaptcha,name='checkcaptcha')
]