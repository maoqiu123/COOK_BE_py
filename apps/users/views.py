# Create your views here.
from django.views.generic.base import View
from utils.ResponseTool import response, response_form

from .forms import RegisterForm, LoginForm
from .service import check_email, register, login
from utils.TokenTool import check_token


class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            code = check_email(request.POST.get("email", ""))
            if code == 101:
                return response(101, "邮箱已存在", None)
            register(request)
            return response(1000, "注册成功", None)
        else:
            return response_form(1001, register_form.errors, None)


class TestView(View):
    def post(self, request):
        print(request.user)
        data = {"token": request.my_user.token}
        return response(1000, "token验证成功", data)



class LoginView(View):
    def get(self):
        pass

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            token = login(request)
            if token == 102:
                return response(102, "登录失败，邮箱账号不存在", None)
            elif token == 2001:
                return response(2001, "账户密码不匹配", None)
            data = {"token": token}
            return response(1000, "登录成功", data)
        else:
            return response_form(1001, login_form.errors, None)





