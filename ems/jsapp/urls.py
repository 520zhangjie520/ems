from django.urls import path
from jsapp  import views
urlpatterns = [
    path("index/",views.index,name="index"),
    path("query/",views.query,name="query"),
]