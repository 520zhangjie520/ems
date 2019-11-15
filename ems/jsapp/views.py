from django.shortcuts import render
import json

from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from jsapp.models import User2

# Create your views here.

def index(request):
    return render(request,'index.html')

def query(request):
    print(121)
    name=request.POST.get("name")
    print(name)
    a = User2.objects.filter(name__icontains=name)
    def userdefualt(u):
        if isinstance(u,User2):
            return {"id":u.id,"name":u.name,"age":u.age,"salary":str(u.salary),"birthday":u.brithday.strftime("%Y-%m-%d %H:%M:%S")}
    return JsonResponse({"users": list(a)}, json_dumps_params={"default": userdefualt})

