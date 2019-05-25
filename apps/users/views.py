# Create your views here.
from django.views.generic.base import View
from utils.ResponseTool import response, response_form, response_object

from .forms import RegisterForm, LoginForm, UserUpdateForm
from .service import check_email, register, login, update_user, get_user
from utils.cacheTool import test
from dwebsocket.decorators import accept_websocket


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


class LoginView(View):
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


class UserView(View):
    def get(self, request):
        user = get_user(request)
        return response(1000, "查询用户信息成功", user)

    def put(self, request):
        user_update_form = UserUpdateForm(request.PUT)
        if user_update_form.is_valid():
            update_user(request)
            return response(1000, '修改用户信息成功', None)
        else:
            return response_form(1001, user_update_form.errors, None)


class TestView(View):
    @accept_websocket
    def post(self, request):
        test()
        return response(1000, "test")
