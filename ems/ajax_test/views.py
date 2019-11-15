from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from ajax_test.models import Ajax_user
import random,os,string
from captcha.image import ImageCaptcha
# Create your views here.
def regist(request):
    return render(request, 'ajax_regist.html')
def registlogic(request):
    try:
        with transaction.atomic():
            name=request.POST.get('name')
            password=int(request.POST.get('password'))
            print(name,password)
            res=Ajax_user.objects.create(name=name,password=password)
            print(res)
            if res:
                return HttpResponse('注册成功')
    except:
        return HttpResponse('注册失败')
#=====用户名判断======
def checkname(request):
    name=request.POST.get('name')
    print(name)
    res=Ajax_user.objects.filter(name=name)
    if res:
        return HttpResponse('0')
    else:
        return HttpResponse('1')
#======验证码验证=======
def  checkcaptcha(request):
    cap=request.session.get('captcha')
    c_cap=request.POST.get('cap')
    if cap.lower()==c_cap.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')

def getcaptcha(request):
    code=random.sample(string.ascii_letters+string.digits,4)
    re_code=''.join(code)
    request.session['captcha']=re_code
    capt=ImageCaptcha().generate(re_code)
    return HttpResponse(capt,'image/png')