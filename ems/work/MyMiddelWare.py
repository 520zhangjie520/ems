from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        print("init1")

    # view处理请求前执行
    def process_request(self, request):  # 某一个view

        print("request:", request)

    # 在process_request之后View之前执行
    def process_view(self, request, view_func, view_args, view_kwargs):
        #过滤掉登录页面的请求和注册页面的请求  是不是登录请求和注册请求
        print(request.path)
        # if request.path == "/middleware/login/" or request.path == "/middleware/regist/" :
        # if "login" in request.path or "regist" in request.path or "admin" in request.path:
        #     pass
        # else:
        #     status = request.session.get("login")
        #     if status:
        #         print("正在登录中....")
        #     else:
        #         return redirect("login ")


    # view执行之后，响应之前执行
    def process_response(self, request, response):
        print("response:", request, response)
        return response  # 必须返回response

    # 如果View中抛出了异常
    def process_exception(self, request, ex):  # View中出现异常时执行
        print("exception:", request, ex)