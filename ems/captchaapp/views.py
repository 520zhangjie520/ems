from django.shortcuts import render,HttpResponse
from captchaapp.captcha.image import ImageCaptcha
import random,string
# Create your views here.

def getcaptcha(request):
    # 生成一个图片验证码的对象
    image = ImageCaptcha()
    # 生成随机数
    code = random.sample(string.ascii_letters+string.digits,5)
    code = "".join(code)
    print(code)
    request.session["code"] = code
    data = image.generate(code)
    return HttpResponse(data,"image/png")


def regist(request):
    return render(request,"captchaapp/regist.html")

def checkcaptcha(request):
    input_code = request.POST.get("captcha")
    session_code = request.session.get("code")
    if input_code.upper() == session_code.upper():
        return HttpResponse("验证码正确")
    return HttpResponse("验证码错误")