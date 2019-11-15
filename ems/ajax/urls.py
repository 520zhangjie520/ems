from django.urls import path
from ajax import views
app_name='ajax'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('query/',views.query,name='query'),
]











