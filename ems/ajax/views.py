import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ajax.models import User
# Create your views here.


def index(request):
    return render(request,'index.html')


def query(request):
    name=request.POST.get("name")
    users = User.objects.filter(name__icontains=name)

    def userdefualt(u):
        if isinstance(u,User):
            return {"id":u.id,"name":u.name,"age":u.age,"salary":str(u.salary),"birthday":u.brithday.strftime("%Y-%m-%d %H:%M:%S")}
    return JsonResponse({"users": list(users)}, json_dumps_params={"default": userdefualt})
