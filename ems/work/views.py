from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import HttpResponse, redirect, render
from work.models import User1,news1
from captchaapp.captcha.image import ImageCaptcha
import random,string
import uuid,os

# 渲染登陆界面
# Render login screen
def login(request):
    # 在登陆界面读取本地的cookie信息。
    name=request.COOKIES.get('username')
    if name:
        # 获取name进行解码编码
        name=name.encode('latin-1').decode('utf-8')
    pwd=request.COOKIES.get('password')
    # 判断从cookie中读取的信息在没在数据库
    res=User1 .objects.filter(name=name,password=pwd)
    # 判断名字和密码是不是存在数据库
    if res:
        # 登陆成功后保持登陆状态为真
        request.session['login'] = 'ok'
        return redirect('home')
    return render(request,'login.html' )

# 登陆界面的视图函数
def login1(request):
    username = request.POST.get('name')
    pwd = request.POST.get('password')
    rem = request.POST.get('remember')
    res = User1.objects.filter(username=username,password=pwd)
    # 判断登陆否
    if res:
        # 重定向返回到主界面
        response = redirect('home')
        # 存储session为了进行页面数据共享
        request.session['login'] = 'ok'
        if rem:
            # 如果登陆成功，就往cookie中存值
            response.set_cookie('username'.encode('utf-8').decode('latin-1'),username ,max_age= 24*7*3600)
            response.set_cookie('password'.encode('utf-8').decode('latin-1'),pwd , max_age=24 * 7 * 3600)
            print('22')
        return response
    else:
        # 返回到你的ajax函数中进行判断
        return  HttpResponse ('0')

# 注册
def regist(request):
    # 进入注册界面
    return  render(request,'regist.html')

# 检查重复名
def checkname(request):
    name=request.POST.get('name')
    res=User1.objects.filter(name=name )
    # 返回给注册界面ajax函数的值
    if res:
        return HttpResponse('1')
    else:
        return HttpResponse('0')

# 进行验证码的判断
def checkpic(request):
    # 获取验证码的字符串
    pic=request.session.get('code')
    # 获取html的验证码
    b=request.POST.get('captcha')
    # 返回给注册界面ajax函数的值
    if pic.lower()==b.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')
# 注册的逻辑函数
def regist1(request):
    # 得到注册界面的请求，获取信息，放入数据库
    with transaction.atomic():
        username=request.POST.get('username')
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        sex=request.POST.get('sex')
        input_code = request.POST.get("cap")
        session_code = request.session.get("code")

        res = User1.objects.create(username=username , name=name,password=pwd,sex=sex, )
        if res or input_code.upper() == session_code.upper():
            # 注册成功进行跳转
            return  HttpResponse('1')
        else:
            return HttpResponse('0')

# 主页面
def home(request):
    stu=request.session.get('login')
    num=request.session.get('number',1)
    number = request.GET.get("number",num)
    # 只有登陆成功以后才会进入主页面，否则就在登陆页面
    user= news1.objects.all()
    pagtor = Paginator(object_list=user , per_page=2)
    page = pagtor.page(number)
    # print(pagtor)
    if stu :
        return render(request,'emplist.html',{'page':page})
    return redirect('login')

def home1(request):
    return render(request,'addEmp.html' )

def add(request):
    # 返回到你的添加界面
    return render(request,'addEmp.html' )

def addemp(request):
    # 获取add界面的信息
    name=request.POST.get('name')
    salary=request.POST.get('salary')
    age=request.POST.get('age')
    headpic = request.FILES.get("headpic")
    ext = os.path.splitext(headpic.name)[1]
    headpic.name = str(uuid.uuid4()) + ext
    a=news1.objects.create(name=name,salary=salary,age=age,headpic=headpic)
    user = news1.objects.all()
    # 进行分页
    pagtor = Paginator(object_list=user , per_page=2)
    request.session['number']=pagtor.num_pages
    if a :
        return redirect('home')
    return render(request,'addEmp.html' )
def getcaptcha(request):
    # 生成一个图片验证码的对象
    image = ImageCaptcha()
    # print(image)
    # 生成随机数
    code = random.sample(string.ascii_letters+string.digits,1)
    # 把获取的列表进行字符串拼接
    code = "".join(code)
    # print(code)
    # 把你的字符串放入session中  ，方便进行验证
    request.session["code"] = code
    # 把验证码放入你的图片里
    data = image.generate(code)
    # 把验证码图片返回到html界面
    return HttpResponse(data,"image/png")

def update(request):
    # print('看这里')
    id=request.GET.get('id')
    number=request.GET.get('num')
    request.session['number']=number
    data=news1.objects.get(id=id)
    # print(data.name)
    return render(request,'updateEmp.html',{'data':data})

def update1(request):
    a = request.GET.get("id")
    data = news1.objects.get(id=a)
    headpic1 = request.FILES.get("headpic")
    if headpic1 :
        ext = os.path.splitext(headpic1.name)[1]
        headpic1.name = str(uuid.uuid4()) + ext
        data.headpic = headpic1
    data.name = request.POST.get("name")
    data.age = request.POST.get("age")
    data.salary = request.POST.get("salary")
    data.save()
    return redirect('home')

def del1(request):
    a= request.GET.get("id")
    number = request.GET.get('num')
    request.session['number'] = number
    news1.objects.get(id=a).delete()
    return redirect( 'home')

#======验证码验证=======
def  checkcaptcha(request):
    cap=request.session.get('code')
    c_cap=request.POST.get('cap')
    if cap.lower()==c_cap.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')






